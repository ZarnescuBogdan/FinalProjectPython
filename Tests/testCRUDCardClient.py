from Domain.cardClient import CardClient

from Repository.repositoryJson import RepositoryJson
from utils import clear_file


def testCardClientRepository():
    filename = "testCardClientRepository.json"
    clear_file(filename)
    cardClientRepositoryJson = RepositoryJson(filename)
    assert cardClientRepositoryJson.read() == []

    cardClient = CardClient("1", "Zarnescu", "Bogdan", "5020622170123",
                            "22.06.2002", "21.11.2021", 0)
    cardClientRepositoryJson.adauga(cardClient)
    assert cardClientRepositoryJson.read("1") == cardClient

    cardClientModificat = CardClient("1", "Zarnescu", "Bibi", "5020622170123",
                                     "22.06.2002", "21.11.2021", 0)
    cardClientRepositoryJson.modifica(cardClientModificat)
    assert cardClientRepositoryJson.read("1") == cardClientModificat

    idDeSters = "1"
    cardClientRepositoryJson.sterge(idDeSters)
    assert cardClientRepositoryJson.read() == []
