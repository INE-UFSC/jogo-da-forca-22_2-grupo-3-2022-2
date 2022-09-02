import string
class Checker:
    '''Classe que implementa a lógica de verificação de palavras e letras para o jogo da forca.

Métodos Publicos Disponíveis

getWord -- Retorna uma string contendo a palavra aleatória contida no Checker.
getSuccessfullWord -- Retorna uma string contendo a palavra aleatória com as letras não encontradas até o momento como "_".
check -- Retorna True caso a letra inserida esteja contida na palavra checker (a letra inserida pode conter acentos e letras maísculas.)
getLetters -- Retorna uma string com as letras do alfabeto, com as letras já utilizadas representadas por "#"
printLetters -- Printa no console as "Letras Disponíveis: " seguido pelas letras em si (getLetters)
'''

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
                self._successfullWord[i] = letter.upper()

    def getSuccessfullWord(self) -> str:
        return "".join(self._successfullWord)

    def check(self, letter) -> bool:
        cleanLetter = letter.lower().replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        print(cleanLetter)
        if cleanLetter not in self._clean_word: # Se a letra não estiver na palavra
            self._letters = self._letters.replace(cleanLetter, '-')
            self._modifyWord(cleanLetter)
            return False
        else: # Se a letra estiver na palavra e já não estiver sido inserida
            self._letters = self._letters.replace(cleanLetter, '-')
            self._modifyWord(cleanLetter)
            return True

    def getLetters(self) -> str:
        return self._letters

    def printLetters(self) -> None:
        retString = " ".join(self._letters).upper()

        print("Letras Disponíveis: " + retString)

if __name__ == "__main__":
    checker = Checker("amigo")
    checker.check("a")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("m")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("i")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("g")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("g")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("u")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("í")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("g")
    print(checker.getSuccessfullWord())
    checker.printLetters()
    checker.check("o")
    print(checker.getSuccessfullWord())
    checker.printLetters()



    