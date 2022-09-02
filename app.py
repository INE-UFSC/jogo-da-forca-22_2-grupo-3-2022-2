from curses.ascii import isdigit
from Game import Game
from Word import Word

while True:
    palavra_gerada = Word().getRandomWord()
    # print(palavra_gerada.getRandomWord())

    jogo = Game(palavra_gerada)
    jogo.run()

    continuar = str(input("Deseja jogar mais uma rodada? [S/N] ")).upper()
    while continuar != 'S' or continuar != 'N':
        continuar = str(input("Entrada inválida! Deseja jogar mais uma rodada? [S/N] ")).upper()
    
    if continuar == 'N':
        break