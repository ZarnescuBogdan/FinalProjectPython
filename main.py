from Domain.cardClientValidator import CardClientValidator
from Domain.filmValidator import FilmValidator

from Repository.repositoryJson import RepositoryJson
from Service.cardClientService import CardClientService
from Service.cautareFullText import CautareFullText
from Service.filmService import FilmService
from Service.generator import Generator
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService
from Tests.testAll import testAll
from UI.console import Consola


def main():
    undoRedoService = UndoRedoService()

    filmRepositoryJson = RepositoryJson("filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepositoryJson, filmValidator,
                              undoRedoService)

    cardClientRepositoryJson = RepositoryJson("carduriClienti.json")
    cardClientValidator = CardClientValidator()
    cardClientService = CardClientService(cardClientRepositoryJson,
                                          cardClientValidator, undoRedoService)

    rezervareRepositoryJson = RepositoryJson("rezervari.json")
    rezervareService = RezervareService(
        rezervareRepositoryJson,
        filmRepositoryJson,
        cardClientRepositoryJson,
        undoRedoService)

    cautareFullText = CautareFullText(filmService, cardClientService)

    generator = Generator()

    consola = Consola(
        filmService,
        cardClientService,
        rezervareService,
        cautareFullText,
        generator,
        undoRedoService)

    consola.runMenu()


if __name__ == '__main__':
    testAll()

    main()
