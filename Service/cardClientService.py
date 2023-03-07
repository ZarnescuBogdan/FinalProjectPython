from Domain.addOperation import AddOperation
from Domain.cardClient import CardClient
from Domain.cardClientValidator import CardClientValidator
from Domain.deleteOperation import DeleteOperation
from Domain.modifyOperation import ModifyOperation

from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class CardClientService:
    def __init__(self,
                 cardClientRepository: Repository,
                 cardClientValidator: CardClientValidator,
                 undoRedoService: UndoRedoService):
        """
        Initializeaza metoda privata cardClientRepository,
        si cardClientValidator.
        :param cardClientRepository: clasa CardClientRepository
        :param cardClientValidator: clasa CardClientValidator
        """
        self.__cardClientRepository = cardClientRepository
        self.__cardClientValidator = cardClientValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        """
        Obtine toate cardurile clienti.
        :return: lista de carduri clienti
        """
        return self.__cardClientRepository.read()

    def adauga(self, idCardClient, nume, prenume, CNP,
               dataNasterii, dataInregistrarii, puncteAcumulate):
        """
        Adauga un card client in lista de carduri clienti.
        :param idCardClient: id-ul cardului client
        :param nume: numele detinatorului de card client
        :param prenume: prenumele detinatorului de card client
        :param CNP: CNP-ul detinatorului de card client
        :param dataNasterii: data nasterii detinatorului de card client
        :param dataInregistrarii: data inregistrarii cardului client
        :param puncteAcumulate: punctele acumulate
        :return: None
        """
        cardClient = CardClient(
            idCardClient,
            nume,
            prenume,
            CNP,
            dataNasterii,
            dataInregistrarii,
            puncteAcumulate)

        carduriClienti = self.getAll()

        for cardCl in carduriClienti:
            if CNP == cardCl.CNP:
                raise ValueError("Exista deja un card client cu CNP-ul dat!")

        self.__cardClientValidator.valideaza(cardClient)
        self.__cardClientRepository.adauga(cardClient)
        self.__undoRedoService.addUndoOperation(AddOperation(
            self.__cardClientRepository, cardClient))

    def sterge(self, idCardClient):
        """
        Sterge un card client din lista de carduri clienti
        :param idCardClient: id-ul cardului client de sters
        :return: None
        """
        cardClient = self.__cardClientRepository.read(idCardClient)
        self.__cardClientRepository.sterge(idCardClient)
        self.__undoRedoService.addUndoOperation(DeleteOperation(
            self.__cardClientRepository, cardClient))

    def modifica(self,
                 idCardClient,
                 nume,
                 prenume,
                 CNP,
                 dataNasterii,
                 dataInregistrarii,
                 puncteAcumulate):
        """
        Modifica un card client din lista de carduri clienti
        :param idCardClient: id-ul cardului client de modificat
        :param nume: noul nume al detinatorului de card client
        :param prenume: noul prenume al detinatorului de card client
        :param CNP: noul CNP al detinatorului de card client
        :param dataNasterii: noua data a nasterii pt detinatorul de cardClient
        :param dataInregistrarii: noua data a inregistrarii a cardului client
        :param puncteAcumulate: noile puncte acumulate
        :return: None
        """
        cardClientVechi = self.__cardClientRepository.read(idCardClient)
        cardClientNou = CardClient(
            idCardClient,
            nume,
            prenume,
            CNP,
            dataNasterii,
            dataInregistrarii,
            puncteAcumulate)

        carduriClienti = self.__cardClientRepository.read()
        for cardCl in carduriClienti:
            if CNP == cardCl.CNP and cardCl.idEntitate != idCardClient:
                raise ValueError("Exista deja un card client cu CNP-ul dat!")

        self.__cardClientValidator.valideaza(cardClientNou)
        self.__cardClientRepository.modifica(cardClientNou)
        self.__undoRedoService.addUndoOperation(ModifyOperation(
            self.__cardClientRepository, cardClientVechi, cardClientNou))

    def carduriOrdDescNrPct(self):
        """
        Ordoneaza lista de carduri clienti descrescator dupa
        numarul de puncte acumulate.
        :return: Lista de carduri clienti ordonata descrescator
                dupa numarul de puncte acumulate
        """
        return sorted(self.__cardClientRepository.read(),
                      key=lambda cardClient: cardClient.puncteAcumulate,
                      reverse=True)
