from Domain.rezervare import Rezervare

from Repository.repositoryJson import RepositoryJson
from utils import clear_file


def testRezervareRepository():
    filename = "testRezervareRepository.json"
    clear_file(filename)
    rezervareRepositoryJson = RepositoryJson(filename)
    assert rezervareRepositoryJson.read() == []

    rezervare = Rezervare("1", "1", "1", "21.11.2021 18:30")
    rezervareRepositoryJson.adauga(rezervare)
    assert rezervareRepositoryJson.read("1") == rezervare

    rezervareModificata = Rezervare("1", "2", "2", "22.11.2021 19:45")
    rezervareRepositoryJson.modifica(rezervareModificata)
    assert rezervareRepositoryJson.read("1") == rezervareModificata

    idDeSters = "1"
    rezervareRepositoryJson.sterge(idDeSters)
    assert rezervareRepositoryJson.read() == []
