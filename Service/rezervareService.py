from Domain.addOperation import AddOperation
from Domain.cardClient import CardClient
from Domain.deleteOperation import DeleteOperation
from Domain.film import Film
from Domain.modifyOperation import ModifyOperation
from Domain.multiDelFilmResOperation import \
    MultiDelFilmResOperation
from Domain.multiDeleteOperation import MultiDeleteOperation
from Domain.rezervare import Rezervare

from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService
from utils import Utils


class RezervareService:
    def __init__(self,
                 rezervareRepository: Repository,
                 filmRepository: Repository,
                 cardClientRepository: Repository,
                 undoRedoService: UndoRedoService):
        """
        Initializeaza metodele private rezervareRepository, filmRepository,
        si cardClientRepository.
        :param rezervareRepository: clasa RezervareRepository
        :param filmRepository: clasa FilmRepository
        :param cardClientRepository: clasa CardClientRepository
        """
        self.__rezervareRepository = rezervareRepository
        self.__filmRepository = filmRepository
        self.__cardClientRepository = cardClientRepository
        self.__undoRedoService = undoRedoService

    def getAll(self):
        """
        Obtine toate rezervarile.
        :return: lista de rezervari
        """
        return self.__rezervareRepository.read()

    def adauga(self,
               idRezervare,
               idFilm,
               idCardClient,
               dataOra):
        """
        Adauga o rezervare in lista de rezervari.
        :param idRezervare: id-ul rezervarii
        :param idFilm: id-ul filmului
        :param idCardClient: id-ul cardului client
        :param dataOra: data si ora pentru care se face rezervarea
        :return: None
        """
        if self.__filmRepository.read(idFilm) is None:
            raise KeyError("Nu exista niciun film cu id-ul dat!")
        film: Film
        film = self.__filmRepository.read(idFilm)
        if film.inProgram == "nu":
            raise ValueError("Filmul nu mai este in program!")
        if self.__cardClientRepository.read(idCardClient) is None:
            raise ValueError("Cardul client cu id-ul dat nu exista!")

        rezervare = Rezervare(
            idRezervare,
            idFilm,
            idCardClient,
            dataOra
        )
        self.__rezervareRepository.adauga(rezervare)
        self.__undoRedoService.addUndoOperation(AddOperation(
            self.__rezervareRepository, rezervare))

        if idCardClient is not None and \
                self.__cardClientRepository.read(idCardClient) is not None:
            cardClient: CardClient
            cardClient = self.__cardClientRepository.read(idCardClient)
            cardClient.puncteAcumulate += int(film.pretBilet // 10)
            self.__cardClientRepository.modifica(cardClient)

    def sterge(self, idRezervare):
        """
        Sterge o rezervare din lista de rezervari.
        :param idRezervare: id-ul rezervarii de sters
        :return: None
        """
        rezervare: Rezervare
        rezervare = self.__rezervareRepository.read(idRezervare)

        self.__rezervareRepository.sterge(idRezervare)
        self.__undoRedoService.addUndoOperation(DeleteOperation(
            self.__rezervareRepository, rezervare))

        if rezervare.idCardClient is not None:
            film: Film
            film = self.__filmRepository.read(rezervare.idFilm)
            cardClient: CardClient
            cardClient = self.__cardClientRepository.read(
                rezervare.idCardClient)
            cardClient.puncteAcumulate -= int(film.pretBilet // 10)

    def modifica(self,
                 idRezervare,
                 idFilm,
                 idCardClient,
                 dataOra):
        """
        Modifica o rezervare din lista de rezervari.
        :param idRezervare: id-ul rezervarii de modificat
        :param idFilm: noul id al filmului
        :param idCardClient: noul id al cardului client
        :param dataOra: noua data si ora
        :return: None
        """
        if self.__filmRepository.read(idFilm) is None:
            raise KeyError("Nu exista niciun film cu id-ul dat!")
        film: Film
        film = self.__filmRepository.read(idFilm)
        if film.inProgram == "nu":
            raise ValueError("Filmul nu mai este in program!")
        if self.__cardClientRepository.read(idCardClient) is None:
            raise ValueError("Cardul client cu id-ul dat nu exista!")

        rezervareInitiala: Rezervare
        rezervareInitiala = self.__rezervareRepository.read(idRezervare)
        cardClientInitial: CardClient
        cardClientInitial = self.__cardClientRepository.read(
            rezervareInitiala.idCardClient)

        rezervare = Rezervare(
            idRezervare,
            idFilm,
            idCardClient,
            dataOra
        )
        self.__rezervareRepository.modifica(rezervare)
        self.__undoRedoService.addUndoOperation(ModifyOperation(
            self.__rezervareRepository, rezervareInitiala, rezervare))

        if cardClientInitial is not None:
            filmInitial: Film
            filmInitial = self.__filmRepository.read(rezervareInitiala.idFilm)
            if idCardClient == cardClientInitial.idEntitate:
                cardClientInitial.puncteAcumulate -= int(filmInitial.pretBilet
                                                         // 10)
                cardClientInitial.puncteAcumulate += int(film.pretBilet // 10)
                self.__cardClientRepository.modifica(cardClientInitial)
            else:
                cardClient: CardClient
                cardClient = self.__cardClientRepository.read(idCardClient)
                cardClientInitial.puncteAcumulate -= int(filmInitial.pretBilet
                                                         // 10)
                cardClient.puncteAcumulate += int(film.pretBilet // 10)

    def rezervariDinIntervalOrar(self, intervalOrar):
        """
        Determina toate rezervarile dintr-un interval orar dat.
        :param intervalOrar: intervalul orar dat
        :return: lista cu rezervarile din intervalul orar dat
        """
        rezultat = []
        for rezervare in self.__rezervareRepository.read():
            dataOraAsList = rezervare.dataOra.split(" ")
            oraMinut = dataOraAsList[1].split(":")
            ora = int(oraMinut[0])
            if ora >= intervalOrar[0] and ora <= intervalOrar[1]:
                rezultat.append(rezervare)
        return rezultat

    def filmeOrdonateDescNrRez(self):
        """
        Determina lista de filme ordonate descrescator
        dupa numarul de rezervari.
        :return: lista de filme ordonate descrescator
                dupa numarul de rezervari
        """
        numarRezervari = {}
        rezultat = []
        for film in self.__filmRepository.read():
            numarRezervari[film.idEntitate] = []
        for rezervare in self.getAll():
            numarRezervari[rezervare.idFilm].append(rezervare)

        for idFilm in numarRezervari:
            rezervari = numarRezervari[idFilm]
            rezultat.append(
                {
                    "film": self.__filmRepository.read(idFilm),
                    "numarRezervari": len(rezervari)
                }
            )
        ''' return sorted(rezultat, key=lambda nrRezervari:
                              nrRezervari["numarRezervari"], reverse=True)'''
        return Utils.sort(rezultat, key=lambda nrRezervari:
                          nrRezervari["numarRezervari"], reverse=True)

    def stergereCascada(self, idFilm):
        try:
            film: Film
            film = self.__filmRepository.read(idFilm)
            if film is None:
                raise ValueError("Filmul cautat nu exista!")
            rezervari = self.getAll()
            rezervariSterse = []
            for rezervare in rezervari:
                if rezervare.idFilm == idFilm and film.idEntitate == idFilm:
                    rezervariSterse.append(rezervare)
                    self.__rezervareRepository.sterge(rezervare.idEntitate)
            self.__filmRepository.sterge(idFilm)
            self.__undoRedoService.addUndoOperation(
                MultiDelFilmResOperation(self.__filmRepository,
                                         self.__rezervareRepository, film,
                                         rezervariSterse))

        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def stergeRezervari(self, intervalZile):
        intervalZile = intervalZile.split("-")
        if len(intervalZile) != 2:
            raise ValueError("Intervalul de zile trebuie sa contina 2 "
                             "zile pentru a contine un interval!")
        intervalZile[0] = int(intervalZile[0])
        intervalZile[1] = int(intervalZile[1])
        intervalZile: list[int]
        if intervalZile[0] > intervalZile[1]:
            raise ValueError("Intervalul de zile trebuie sa fie "
                             "crescator!")
        rezervariSterse = []
        for rezervare in self.getAll():
            dataOraAsList = rezervare.dataOra.split(" ")
            dataAsList = dataOraAsList[0].split(".")
            ziua = int(dataAsList[0])
            if ziua >= intervalZile[0] and ziua <= intervalZile[1]:
                rezervariSterse.append(rezervare)
                self.__rezervareRepository.sterge(rezervare.idEntitate)
        self.__undoRedoService.addUndoOperation(MultiDeleteOperation(
            self.__rezervareRepository, rezervariSterse))
