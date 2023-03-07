import random

import jsonpickle


class Generator:
    def genereazaId(self):
        """
        Aceasta metoda creeaza un id random pt fiecare film.
        :return:o valoare random
        """
        filme: dict
        filename = "filme.json"
        file = open(filename)
        jsonStr = file.read()
        list = []
        try:
            filme = jsonpickle.decode(jsonStr)
            for i in filme.keys():
                list.append(filme[i].idFilm)
        except Exception:
            pass

        file.close()

        while True:
            id = str(random.randint(1, 150))
            if id in list:
                continue
            else:
                return id

    def genereazaTitlu(self):
        """
        Aceasta metoda alege un titlu random dintr-o lista predefinita.
        :return: o valoare random
        """
        numePosibile = ["Avengers", "Fast&Furious", "Saw", "It", "Hellboy",
                        "The Conjuring", "Spiderman", "Red Notice",
                        "Beetlejuice", "The Mask", "The Godfather",
                        "StarWars"]
        return random.choice(numePosibile)

    def genereazaAnAp(self):
        """
        Aceasta metoda alege un an aparitie random dintr-o lista predefinita.
        :return: o valoare random
        """
        anAparitie = ["2000", "2001", "2002", "2003", "2004", "2005", "2006",
                      "2007", "2008", "2009", "2010", "2011", "2012", "2013",
                      "2014", "2015", "2016", "2017", "2018", "2019", "2020",
                      "2021"]
        return random.choice(anAparitie)

    def genereazaPrBil(self):
        """
        Aceasta metoda alege un pret al biletului
        random dintr-o lista predefinita.
        :return: o valoare random
        """
        pretBilet = [15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0,
                     19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5,
                     24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0,
                     28.5, 29.0, 29.5, 30.0]
        return random.choice(pretBilet)

    def genereazaInPr(self):
        """
        Aceasta metoda alege valoarea pentru atributul inProgram
        random dintre 'da' si 'nu'."
        :return: o valoare random
        """
        inProgram = ["da", "nu"]
        return random.choice(inProgram)
