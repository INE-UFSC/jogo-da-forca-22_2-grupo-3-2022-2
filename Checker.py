"""Classe que implementa a lógica de verificação de palavras e letras para o jogo da forca.

Métodos Publicos Disponíveis

getWord -- Retorna uma string contendo a palavra aleatória contida no Checker.
getSuccessfullWord -- Retorna uma string contendo a palavra aleatória com as letras não encontradas até o momento como "_".
check -- Retorna True caso a letra inserida esteja contida na palavra checker (a letra inserida pode conter acentos e letras maísculas.)
getLetters -- Retorna uma string com as letras do alfabeto, com as letras já utilizadas representadas por "#"
printLetters -- Printa no console as "Letras Disponíveis: " seguido pelas letras em si (getLetters)
"""

import string
class Checker:
    def __init__(self, word):
        self._word = word
        self._successfullWord = ["_" for _ in range(len(self._word))]
        self._clean_word = word.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        self._letters = string.ascii_lowercase

    def getWord(self) -> str:
        return self._word
    
    def _modifyWord(self, letter):
        for i in range(len(self._word)):
            if self._word[i] == letter:
                self._successfullWord[i] = letter

    def getSuccessfullWord(self) -> str:
        return "".join(self._successfullWord)

    def check(self, letter) -> bool:
        cleanLetter = letter.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        if cleanLetter in self._clean_word:
            self._letters = self._letters.replace(cleanLetter, '#')
            self._modifyWord(cleanLetter)
            return True
        else:
            return False

    def getLetters(self) -> str:
        return self._letters

    def printLetters(self) -> None:
        retString = ", ".join(self._letters).upper()

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
    checker.check("i")
    checker.printLetters()
    print(checker.getSuccessfullWord())
    checker.check("g")
    checker.printLetters()
    print(checker.getSuccessfullWord())
    checker.check("o")
    checker.printLetters()
    print(checker.getSuccessfullWord())


    