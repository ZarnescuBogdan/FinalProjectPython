from Domain.film import Film

from Repository.repositoryJson import RepositoryJson
from utils import clear_file


def testFilmRepository():
    filename = "testFilmRepository.json"
    clear_file(filename)
    filmRepositoryJson = RepositoryJson(filename)
    assert filmRepositoryJson.read() == []

    film = Film("1", "Fast&Furious", "2008", 30.0, "da")
    filmRepositoryJson.adauga(film)
    assert filmRepositoryJson.read("1") == film

    filmModificat = Film("1", "AlbaCaZapada", "1960", 10, "nu")
    filmRepositoryJson.modifica(filmModificat)
    assert filmRepositoryJson.read("1") == filmModificat

    idDeSters = "1"
    filmRepositoryJson.sterge(idDeSters)
    assert filmRepositoryJson.read() == []
