from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Film(Entitate):
    """
    Creeaza un film.
    -idFilm: id-ul filmului, trebuie sa fie unic.
    -titlu: titlul filmului.
    -anAparitie: anul in care a aparut filmul.
    -pretBilet: pretul biletului
    -inProgram: da/nu
    """
    titlu: str
    anAparitie: str
    pretBilet: float
    inProgram: str
