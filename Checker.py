#classe checker recebe a palavra gerada e realiza os processos de checagem
import string
from Words import Words

class Checker:
    def __init__(self, word):
        self._word = word
        self._successfullWord = "_"*len(self._word)
        self._clean_word = word.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        self._letters = string.ascii_lowercase

    def getWord(self):
        return self._word
    
    def modifyWord(self, letter):
        #TODO
        #Modificar letra da palavra original ao acertar
        for i in range(len(self._word)):
            if self._word[i] == letter:
                successList = list(self.getSuccessfullWord())
                self._successfullWord[i] = self._word[i]

    def getSuccessfullWord(self):
        return self._successfullWord


    def check(self, letter):
        cleanLetter = letter.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        if cleanLetter in self._clean_word:
            self._letters = self._letters.replace(cleanLetter, '#')
            self.modifyWord(cleanLetter)
            return True
        else:
            return False

    def getLetters(self):
        return self._letters

    def printLetters(self):
        retString = ", ".join(self._letters)
        print("Letras Disponíveis: " + retString)

if __name__ == "__main__":
    checker = Checker("amigo")
    print(checker.getSuccessfullWord())
    checker.check("a")
    checker.printLetters()
    print(checker.getSuccessfullWord())
    checker.check("á")
    checker.printLetters()
    print(checker.getSuccessfullWord())
    checker.check("ú")
    checker.check("m")
    checker.printLetters()
    print(checker.getSuccessfullWord())
    


    