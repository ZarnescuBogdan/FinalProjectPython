from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.film import Film
from Domain.filmValidator import FilmValidator
from Domain.modifyOperation import ModifyOperation

from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class FilmService:
    def __init__(self,
                 filmRepository: Repository,
                 filmValidator: FilmValidator,
                 undoRedoService: UndoRedoService):
        """
        Initializeaza metodele private filmRepository, si filmValidator.
        :param filmRepository: clasa FilmRepository
        :param filmValidator: clasa FilmValidator
        """
        self.__filmRepository = filmRepository
        self.__filmValidator = filmValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        """
        Obtine toate filmele.
        :return: lista de filme
        """
        return self.__filmRepository.read()

    def adauga(self, idFilm, titlu, anAparitie, pretBilet, inProgram):
        """
        Adauga un film in lista de filme.
        :param idFilm: id-ul filmului
        :param titlu: titlul filmului
        :param anAparitie: anul in care a aparut filmul
        :param pretBilet: pretul biletului
        :param inProgram: da/nu
        :return: None
        """
        film = Film(idFilm, titlu, anAparitie, pretBilet, inProgram)
        self.__filmValidator.valideaza(film)
        self.__filmRepository.adauga(film)
        self.__undoRedoService.addUndoOperation(AddOperation(
            self.__filmRepository, film))

    def sterge(self, idFilm):
        """
        Sterge un film din lista de filme
        :param idFilm: id-ul filmului de sters
        :return: None
        """
        film = self.__filmRepository.read(idFilm)
        self.__filmRepository.sterge(idFilm)
        self.__undoRedoService.addUndoOperation(DeleteOperation(
            self.__filmRepository, film))

    def modifica(self, idFilm, titlu, anAparitie, pretBilet, inProgram):
        """
        Modifica un film din lista de filme.
        :param idFilm: id-ul filmului de modificat
        :param titlu: noul titlu al filmului
        :param anAparitie: noul an in care a aparut filmul
        :param pretBilet: noul pret al biletului
        :param inProgram: da/nu
        :return: None
        """
        filmVechi = self.__filmRepository.read(idFilm)
        filmNou = Film(idFilm, titlu, anAparitie, pretBilet, inProgram)
        self.__filmValidator.valideaza(filmNou)
        self.__filmRepository.modifica(filmNou)
        self.__undoRedoService.addUndoOperation(ModifyOperation(
            self.__filmRepository, filmVechi, filmNou))
