#classe checker recebe a palavra gerada e realiza os processos de checagem
import string
from Words import Words

class Checker:
    def __init__(self, word):
        self._word = word
        self._clean_word = word.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        self._letters = string.ascii_lowercase

    def check(self, letter):
        cleanLetter = letter.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        if cleanLetter in self._clean_word:
            self._letters.replace(cleanLetter, '#')
            return True
        else:
            return False

    def letters(self):
        return self._letters

    def printLetters(self):
        retString = "".join(self._letters, ', ')
        print("Letras Disponíveis: " + retString)

if __name__ == "__main__":
    checker = Checker("amigo")
    print(checker.check("a"))
    checker.printLetters()
    print(checker.check("á"))
    checker.printLetters()
    print(checker.check("b"))
    checker.printLetters()

    


    