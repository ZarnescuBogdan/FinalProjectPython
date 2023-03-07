from Domain.entitate import Entitate
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, idEntitate=None):
        """
        Citeste lista de entitati.
        :param idEntitate: id-ul entitatii
        :return: lista de entitati, daca idEntitate este None,
            respectiv, entitatea cu id-ul dat,
            sau None, daca nu exista o entitate cu id-ul dat
        """
        if idEntitate is None:
            return list(self.entitati.values())

        if idEntitate in self.entitati:
            return self.entitati[idEntitate]
        else:
            return None

    def adauga(self, entitate: Entitate):
        """
        Adauga o entitate.
        :param entitate: entitatea care va fi adaugata
        :return: None
        """
        if self.read(entitate.idEntitate) is not None:
            raise ValueError("Exista deja o entitate"
                             " cu id-ul dat!")
        self.entitati[entitate.idEntitate] = entitate

    def sterge(self, idEntitate: str):
        """
        Sterge o entitate.
        :param idEntitate: id-ul entitatii de sters
        :return: None
        """
        if self.read(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        del self.entitati[idEntitate]

    def modifica(self, entitate: Entitate):
        """
        Modifica o entitate.
        :param entitate: entitatea care va fi modificata
        :return: None
        """
        if self.read(entitate.idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self.entitati[entitate.idEntitate] = entitate
