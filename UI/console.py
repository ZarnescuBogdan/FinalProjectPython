import datetime

from Service.cardClientService import CardClientService
from Service.cautareFullText import CautareFullText
from Service.filmService import FilmService
from Service.rezervareService import RezervareService
from Service.generator import Generator
from Service.undoRedoService import UndoRedoService


class Consola:
    def __init__(self,
                 filmService: FilmService,
                 cardClientService: CardClientService,
                 rezervareService: RezervareService,
                 cautareFullText: CautareFullText,
                 generator: Generator,
                 undoRedoService: UndoRedoService):
        """
        Initializeaza metodele private filmService, cardClientService,
        si rezervareService.
        :param filmService: clasa FilmService
        :param cardClientService: clasa CardClientService
        :param rezervareService: clasa RezervareService
        """
        self.__filmService = filmService
        self.__cardClientService = cardClientService
        self.__rezervareService = rezervareService
        self.__cautareFullText = cautareFullText
        self.__generator = generator
        self.__undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1.CRUD filme")
            print("2.CRUD carduri clienti")
            print("3.CRUD rezervari")
            print("4. Căutare filme și clienți. Căutare full text.")
            print("5. Afișarea tuturor rezervărilor dintr-un interval de ore "
                  "dat, indiferent de zi.")
            print("6. Afișarea filmelor ordonate descrescător după numărul "
                  "de rezervări.")
            print("7. Afișarea cardurilor client ordonate descrescător după "
                  "numărul de puncte de pe card.")
            print("8. Ștergerea tuturor rezervărilor dintr-un anumit "
                  "interval de zile.")
            print("9. Incrementarea cu o valoare dată a punctelor de pe toate"
                  " cardurile a căror zi de naștere se află într-un "
                  "interval dat.")
            print("stergere. Stergere cascada.")
            print("random. Generator de n filme.")
            print("u. Undo")
            print("r. Redo")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDFilmeMenu()
            elif optiune == "2":
                self.runCRUDCarduriClientiMenu()
            elif optiune == "3":
                self.runCRUDRezervariMenu()
            elif optiune == "4":
                self.uiCautareFullText()
            elif optiune == "5":
                self.uiRezervariIntervalOrar()
            elif optiune == "6":
                self.uiFilmeOrdonateDescNrRez()
            elif optiune == "7":
                self.uiCarduriOrdDescNrPct()
            elif optiune == "8":
                self.uiStergeRezervari()
            elif optiune == "9":
                self.uiIncrementarePct()
            elif optiune == "stergere":
                self.uiStergereCascada()
            elif optiune == "random":
                self.random_generator()
            elif optiune == "u":
                self.__undoRedoService.undo()
            elif optiune == "r":
                self.__undoRedoService.redo()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDFilmeMenu(self):
        while True:
            print("1. Adauga film")
            print("2. Sterge film")
            print("3. Modifica film")
            print("a. Afiseaza toate filmele")
            print("x. Revenire la meniul principal")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaFilm()
            elif optiune == "2":
                self.uiStergeFilm()
            elif optiune == "3":
                self.uiModificaFilm()
            elif optiune == "a":
                self.showAllFilme()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            anAparitie = input("Dati anul aparitiei: ")
            pretBilet = float(input("Dati pretul biletului: "))
            inProgram = input("Precizati daca filmul este "
                              "in program('da'|'nu'): ")

            self.__filmService.adauga(
                idFilm, titlu, anAparitie, pretBilet, inProgram)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def uiStergeFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de sters: ")

            self.__filmService.sterge(idFilm)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def uiModificaFilm(self):
        try:
            idFilm = input("Dati id-ul filmului de modificat: ")
            titlu = input("Dati noul titlu al filmului: ")
            anAparitie = input("Dati noul an al aparitiei: ")
            pretBilet = float(input("Dati noul pret al biletului: "))
            inProgram = input("Dati noul program al filmului: ")

            self.__filmService.modifica(
                idFilm, titlu, anAparitie, pretBilet, inProgram)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def showAllFilme(self):
        for film in self.__filmService.getAll():
            print(film)

    def runCRUDCarduriClientiMenu(self):
        while True:
            print("1. Adauga card client")
            print("2. Sterge card client")
            print("3. Modifica card client")
            print("a. Afiseaza toate cardurile clientilor")
            print("x. Revenire la meniul principal")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaCardClient()
            elif optiune == "2":
                self.uiStergeCardClient()
            elif optiune == "3":
                self.uiModificaCardClient()
            elif optiune == "a":
                self.showAllCarduriClienti()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaCardClient(self):
        try:
            idCardClient = input("Dati id-ul cardului client: ")
            nume = input("Dati numele detinatorului de card client: ")
            prenume = input("Dati prenumele detinatorului de card client: ")
            CNP = input("Dati CNP-ul detinatorului de card client: ")
            dataNasteriiAsStr = input("Dati data nasterii(dd.mm.yyyy): ")
            dataNasteriiAsDate = datetime.datetime.strptime(dataNasteriiAsStr,
                                                            "%d.%m.%Y")
            dataNasterii = dataNasteriiAsDate.strftime("%d.%m.%Y")
            dataInregAsStr = input("Dati data inregistrarii(dd.mm.yyyy): ")
            dataInregAsDate = datetime.datetime.strptime(dataInregAsStr,
                                                         "%d.%m.%Y")
            dataInregistrarii = dataInregAsDate.strftime("%d.%m.%Y")
            puncteAcumulate = int(input("Dati punctele acumulate: "))

            self.__cardClientService.adauga(
                idCardClient, nume, prenume, CNP,
                dataNasterii, dataInregistrarii, puncteAcumulate)
        except ValueError as ve:
            print(ve)
        except Exception as ex:
            print(ex)

    def uiStergeCardClient(self):
        try:
            idCardClient = input("Dati id-ul cardului client de sters: ")

            self.__cardClientService.sterge(idCardClient)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def uiModificaCardClient(self):
        try:
            idCardClient = input("Dati id-ul cardului client de modificat: ")
            nume = input("Dati noul nume al detinatorului de card client: ")
            prenume = input("Dati noul prenume al detinatorului"
                            "de card client: ")
            CNP = input("Dati noul CNP al detinatorului de card client: ")
            if len(CNP) != 13:
                raise TypeError("CNP-ul trebuie sa contina 13 caractere")
            dataNasteriiAsStr = input("Dati noua data a nasterii"
                                      "(dd.mm.yyyy): ")
            dataNasteriiAsDate = datetime.datetime.strptime(dataNasteriiAsStr,
                                                            "%d.%m.%Y")
            dataNasterii = dataNasteriiAsDate.strftime("%d.%m.%Y")
            dataInregAsStr = input("Dati noua data a inregistrarii"
                                   "(dd.mm.yyyy): ")
            dataInregAsDate = datetime.datetime.strptime(dataInregAsStr,
                                                         "%d.%m.%Y")
            dataInregistrarii = dataInregAsDate.strftime("%d.%m.%Y")
            puncteAcumulate = int(input("Dati noile puncte acumulate: "))

            self.__cardClientService.modifica(
                idCardClient, nume, prenume, CNP,
                dataNasterii, dataInregistrarii, puncteAcumulate)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def showAllCarduriClienti(self):
        for cardClient in self.__cardClientService.getAll():
            print(cardClient)

    def runCRUDRezervariMenu(self):
        while True:
            print("1. Adauga rezervare")
            print("2. Sterge rezervare")
            print("3. Modifica rezervare")
            print("a. Afiseaza toate rezervarile")
            print("x. Revenire la meniul principal")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaRezervare()
            elif optiune == "2":
                self.uiStergeRezervare()
            elif optiune == "3":
                self.uiModificaRezervare()
            elif optiune == "a":
                self.uiShowAllRezervari()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaRezervare(self):
        try:
            idRezervare = input("Dati id-ul rezervarii: ")
            idFilm = input("Dati id-ul filmului: ")
            idCardClient = input("Dati id-ul cardului client: ")
            dataOraAsStr = input("Dati data si ora rezervarii"
                                 "(dd.mm.yyyy HH:MM): ")
            dataOraAsDate = datetime.datetime.strptime(dataOraAsStr,
                                                       "%d.%m.%Y %H:%M")
            dataOra = dataOraAsDate.strftime("%d.%m.%Y %H:%M")
            if idCardClient == "":
                idCardClient = None

            self.__rezervareService.adauga(
                idRezervare,
                idFilm,
                idCardClient,
                dataOra)
            if idCardClient is not None:
                for cardClient in self.__cardClientService.getAll():
                    if idCardClient == cardClient.idEntitate:
                        print(f"Cardul clientului cu id-ul {idCardClient}, "
                              f"are un total de {cardClient.puncteAcumulate} "
                              f"puncte acumulate.")
                        break

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def uiStergeRezervare(self):
        try:
            idRezervare = input("Dati id-ul rezervarii de sters: ")

            self.__rezervareService.sterge(idRezervare)

        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def uiModificaRezervare(self):
        try:
            idRezervare = input("Dati id-ul rezervarii de modificat: ")
            idFilm = input("Dati noul id al filmului: ")
            idCardClient = input("Dati noul id al cardului client: ")
            dataOraAsStr = input("Dati noua data si ora a rezervarii"
                                 "(dd.mm.yyyy HH:MM): ")
            dataOraAsDate = datetime.datetime.strptime(dataOraAsStr,
                                                       "%d.%m.%Y %H:%M")
            dataOra = dataOraAsDate.strftime("%d.%m.%Y %H:%M")
            if idCardClient == "":
                idCardClient = None

            self.__rezervareService.modifica(
                idRezervare,
                idFilm,
                idCardClient,
                dataOra)
            if idCardClient is not None:
                for cardClient in self.__cardClientService.getAll():
                    if idCardClient == cardClient.idEntitate:
                        print(f"Cardul clientului cu id-ul {idCardClient}, "
                              f"are un total de {cardClient.puncteAcumulate} "
                              f"puncte acumulate.")
                        break

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def uiShowAllRezervari(self):
        for rezervare in self.__rezervareService.getAll():
            print(rezervare)

    def random_generator(self):
        try:
            n = int(input("Introduceti numarul de filme generate "
                          "aleatoriu: "))
            for i in range(n):
                self.__filmService.adauga(self.__generator.genereazaId(),
                                          self.__generator.genereazaTitlu(),
                                          self.__generator.genereazaAnAp(),
                                          self.__generator.genereazaPrBil(),
                                          self.__generator.genereazaInPr())

        except ValueError as ve:
            print(f"Eroare: {ve}")

    def uiCautareFullText(self):
        text = input("Dati textul cautat: ")
        print(self.__cautareFullText.cautFullTxt(text))

    def uiRezervariIntervalOrar(self):
        try:
            intervalOrar = input("Dati intervalul orar(de forma HH-HH): ")
            intervalOrar = intervalOrar.split("-")
            if len(intervalOrar) != 2:
                raise ValueError("Intervalul orar trebuie sa contina 2 ore "
                                 "pentru a forma un interval!")
            intervalOrar[0] = int(intervalOrar[0])
            intervalOrar[1] = int(intervalOrar[1])
            if intervalOrar[0] > intervalOrar[1]:
                raise ValueError("Intervalul orar trebuie sa fie crescator!")
            for rezervare in self.__rezervareService.\
                    rezervariDinIntervalOrar(intervalOrar):
                print(rezervare)
        except ValueError as ve:
            print(f"Eroare: {ve}")
        except Exception as ex:
            print(f"Eroare: {ex}")

    def uiFilmeOrdonateDescNrRez(self):
        for film in self.__rezervareService.filmeOrdonateDescNrRez():
            print(film)

    def uiCarduriOrdDescNrPct(self):
        for cardClient in self.__cardClientService.carduriOrdDescNrPct():
            print(cardClient)

    def uiStergeRezervari(self):
        try:
            intervalZile = input("Dati intervalul de zile(de forma ZZ-ZZ): ")
            self.__rezervareService.stergeRezervari(intervalZile)
        except ValueError as ve:
            print(f"Eroare: {ve}")
        except Exception as ex:
            print(f"Eroare: {ex}")

    def uiIncrementarePct(self):
        try:
            valoare = int(input("Dati valoarea cu care se "
                                "incrementeaza punctele: "))
            interval = input("Dati intervalul de zile dat(de forma ZZ-ZZ): ")
            intervalAsList = interval.split("-")
            if len(intervalAsList) != 2:
                raise ValueError("Intervalul dat trebuie sa contina 2 zile "
                                 "pentru a forma un interval!")
            intervalAsList[0] = int(intervalAsList[0])
            intervalAsList[1] = int(intervalAsList[1])
            intervalAsList: list[int]
            if intervalAsList[0] > intervalAsList[1]:
                raise ValueError("Intervalul dat trebuie sa fie crescator!")
            for cardC in self.__cardClientService.getAll():
                dataNasterii = cardC.dataNasterii
                dataNasteriiAsList = dataNasterii.split(".")
                ziua = int(dataNasteriiAsList[0])
                if ziua >= intervalAsList[0] and ziua <= intervalAsList[1]:
                    self.__cardClientService.modifica(cardC.idEntitate,
                                                      cardC.nume,
                                                      cardC.prenume,
                                                      cardC.CNP,
                                                      cardC.dataNasterii,
                                                      cardC.dataInregistrarii,
                                                      cardC.puncteAcumulate +
                                                      valoare)
        except ValueError as ve:
            print(f"Eroare: {ve}")
        except Exception as ex:
            print(f"Eroare: {ex}")

    def uiStergereCascada(self):
        idFilm = input("Dati id-ul filmului de sters: ")
        self.__rezervareService.stergereCascada(idFilm)
