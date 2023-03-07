from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Rezervare(Entitate):
    """
    Creeaza o rezervare.
    -idRezervare: id-ul rezervarii.
    -idFilm: id-ul filmului pentru care se face rezervarea.
    -idCardClient: id-ul cardului client pentru care se face rezervarea.
    -dataOra: data si ora pentru care se face rezervarea.
    """
    idFilm: str
    idCardClient: str
    dataOra: str
