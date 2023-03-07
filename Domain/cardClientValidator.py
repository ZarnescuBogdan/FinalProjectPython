from Domain.cardClient import CardClient


class CardClientValidator:
    def valideaza(self, cardClient: CardClient):
        """
        Valideaza un card client.
        :param cardClient: cardul client care trebuie validat
        :return: None
        """
        if len(cardClient.CNP) != 13:
            raise TypeError("CNP-ul trebuie sa contina 13 caractere!")
