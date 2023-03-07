from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class CardClient(Entitate):
    """
    Creeaza un card client.
    -idCardClient: id-ul cardului client.
    -nume: numele detinatorului de card client.
    -prenume: prenumele detinatorului de card client.
    -CNP: CNP-ul detinatorului de card client.
    -dataNasterii: data nasterii detinatorului de card client.
    -dataInregistrarii: data inregistrarii cardului client.
    -puncteAcumulata: punctele acumulate in card client
    """
    nume: str
    prenume: str
    CNP: str
    dataNasterii: str
    dataInregistrarii: str
    puncteAcumulate: int
