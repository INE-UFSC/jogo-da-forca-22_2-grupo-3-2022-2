#classe checker recebe a palavra gerada e realiza os processos de checagem
import string
from Words import Words

class Checker:
    def __init__(self, word):
        self._word = word
        self._clean_word = word.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        self._letters = list(string.ascii_lowercase) + 'áéíóúç'

    def check(self, letter):
        if letter in self._word:
            self._letters.replace(letter, '#')
            return True
        else:
            return False

    def letters(self):
        return self._letters

    def printLetters(self):
        retString = "".join(self._letters, ', ')
        print("Letras Disponíveis: " + retString)

if __name__ == "__main__":
    pass
    