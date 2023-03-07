from Domain.film import Film
from Domain.filmError import FilmError


class FilmValidator:
    def valideaza(self, film: Film):
        """
        Valideaza un film.
        :param film: filmul care trebuie validat
        :return: None
        """
        erori = []
        if film.pretBilet <= 0:
            erori.append("Pretul biletului trebuie sa fie strict pozitiv!")
        if film.inProgram not in ["da", "nu"]:
            erori.append("Raspunsul la 'Precizati daca filmul este "
                         "in program:' poate fi 'da' sau 'nu'!")
        if len(erori) > 0:
            raise FilmError(erori)
