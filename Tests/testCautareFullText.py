from Domain.cardClient import CardClient
from Domain.cardClientValidator import CardClientValidator
from Domain.film import Film
from Domain.filmValidator import FilmValidator

from Repository.repositoryJson import RepositoryJson
from Service.cardClientService import CardClientService
from Service.cautareFullText import CautareFullText
from Service.filmService import FilmService
from Service.undoRedoService import UndoRedoService
from utils import clear_file


def testCautareFullText():
    filenameFilme = "testFilmRepository.json"
    clear_file(filenameFilme)
    filenameCarduriClienti = "testCardClientRepository.json"
    clear_file(filenameCarduriClienti)

    undoRedoService = UndoRedoService()

    filmRepositoryJson = RepositoryJson(filenameFilme)
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepositoryJson, filmValidator,
                              undoRedoService)

    cardClientRepositoryJson = RepositoryJson(filenameCarduriClienti)
    cardClientValidator = CardClientValidator()
    cardClientService = CardClientService(cardClientRepositoryJson,
                                          cardClientValidator, undoRedoService)

    film = Film("1", "Fast&Furious", "2008", 30.0, "da")
    filmRepositoryJson.adauga(film)

    cardClient = CardClient("1", "Zarnescu", "Bogdan", "5020622170123",
                            "22.06.2002", "21.11.2021", 0)
    cardClientRepositoryJson.adauga(cardClient)

    cautare = CautareFullText(filmService, cardClientService)
    assert cautare.cautFullTxt("9") == {"filme": [],
                                        "carduriClienti": []}
    assert cautare.cautFullTxt("21") == {"filme": [],
                                         "carduriClienti": [cardClient]}
