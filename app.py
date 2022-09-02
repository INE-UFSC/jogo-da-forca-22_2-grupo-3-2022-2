from Game import Game
from Word import Word

while True:
    palavra_gerada = Word().getRandomWord()
    # print(palavra_gerada.getRandomWord())

    jogo = Game(palavra_gerada)
    jogo.run()