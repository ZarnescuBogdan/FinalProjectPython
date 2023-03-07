from Domain.entitate import Entitate
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class MultiDelFilmResOperation(UndoRedoOperation):
    def __init__(self, repositoryFilms: Repository,
                 repositoryReservations: Repository, filmSters: Entitate,
                 rezervariSterse: list[Entitate]):
        self.__repositoryFilms = repositoryFilms
        self.__repositoryReservations = repositoryReservations
        self.__filmSters = filmSters
        self.__rezervariSterse = rezervariSterse

    def doUndo(self):
        self.__repositoryFilms.adauga(self.__filmSters)
        for entitate in self.__rezervariSterse:
            self.__repositoryReservations.adauga(entitate)

    def doRedo(self):
        self.__repositoryFilms.sterge(self.__filmSters.idEntitate)
        for entitate in self.__rezervariSterse:
            self.__repositoryReservations.sterge(entitate.idEntitate)
