import jsonpickle

from Domain.entitate import Entitate
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        """
        Citeste fisierul de entitati.
        :return: lista de entitati
        """
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self):
        """
        Scrie in fisierul de entitati.
        :return: None
        """
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entitati, indent=2))

    def read(self, idEntitate=None):
        """
        Citeste din fisierul de entitati.
        :param idEntitate: id-ul entitatii cautate
        :return: entitatea cu id-ul dat,
            sau None, daca nu exista o entitate cu id-ul dat
        """
        self.entitati = self.__readFile()
        return super().read(idEntitate)

    def adauga(self, entitate: Entitate):
        """
        Adauga o entitate in fisierul de entitati.
        :param entitate: entitatea care va fi adaugata
        :return: None
        """
        self.entitati = self.__readFile()
        super().adauga(entitate)
        self.__writeFile()

    def sterge(self, idEntitate):
        """
        Sterge o entitate din fisierul de entitati.
        :param idEntitate: id-ul entitatii de sters
        :return: None
        """
        self.entitati = self.__readFile()
        super().sterge(idEntitate)
        self.__writeFile()

    def modifica(self, entitate: Entitate):
        """
        Modifica o entitate in fisierul de entitati.
        :param entitate: entitatea modificata
        :return: None
        """
        self.entitati = self.__readFile()
        super().modifica(entitate)
        self.__writeFile()
