from Tests.testCRUDCardClient import testCardClientRepository
from Tests.testCRUDFilm import testFilmRepository
from Tests.testCRUDRezervare import testRezervareRepository
from Tests.testCautareFullText import testCautareFullText


def testAll():
    testFilmRepository()
    testCardClientRepository()
    testRezervareRepository()
    testCautareFullText()
