from Service.cardClientService import CardClientService
from Service.filmService import FilmService


class CautareFullText:
    def __init__(self,
                 filmService: FilmService,
                 cardClientService: CardClientService):
        self.__filmService = filmService
        self.__cardClientService = cardClientService

    def cautFullTxt(self, text):
        """
        Cauta textul dat in lista de filme si in lista de carduri clienti.
        :param text: textul dat
        :return: un dictionar cu filmele, respectiv cardurile clienti care
                contin textul dat in componenta lor.
        """
        filmeCautate = self.cautareFilme(text)
        carduriClientiCautate = self.cautareCarduriClienti(text)
        return {"filme": filmeCautate, "carduriClienti": carduriClientiCautate}

    def cautareFilme(self, text):
        """
        Cauta textul dat in lista de filme.
        :param text: textul dat
        :return: un dictionar cu filmele care contin textul dat
                in componenta lor.
        """
        filme = self.__filmService.getAll()

        filmeCautate = []
        for film in filme:
            if text in film.titlu or text in film.anAparitie or \
                    text in str(film.pretBilet) or text in film.inProgram:
                filmeCautate.append(film)
        return filmeCautate

    def cautareCarduriClienti(self, text):
        """
        Cauta textul dat in lista de carduri clienti.
        :param text: textul dat
        :return: un dictionar cu cardurile clienti care contin textul dat
                in componenta lor.
        """
        carduriClienti = self.__cardClientService.getAll()

        carduriClientiCautate = []
        for cardClient in carduriClienti:
            if text in cardClient.nume or text in cardClient.prenume or \
                    text in cardClient.CNP or \
                    text in cardClient.dataNasterii or \
                    text in cardClient.dataInregistrarii or \
                    text in str(cardClient.puncteAcumulate):
                carduriClientiCautate.append(cardClient)

        return carduriClientiCautate
