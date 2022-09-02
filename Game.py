import string
from Checker import Checker
from desenhos import estagios_desenho_forca as lista_desenho


class Game():
    def __init__(self, palavra, estagios_desenho):
        self.palavra = Checker(palavra)

        self.tentativas = 0
        self.erros = 0
        self.limite_erros = len(estagios_desenho)
        self.desenho_estagios = estagios_desenho  # É possível utlizar diferentes desenhos de console no jogo. Para isso deve-se alterar o import
        self.vitoria = False
        self.finalizou = False
        self.letras_entradas = []  # esta informação está contida na classe Checker pelo método printLetters()
        # o qual printa as letras disponíveis com as letras que foram utilizadas já marcadas

    def run(self):
        running = True
        while running:  # gameloop
            pass
    
    def atualizar_interface(self):
        print("\nRodada atual: {}".format(self.tentativas))
        print(self.desenho_estagios[self.erros])
        print(self.palavra.getSuccessfullWord())
        self.palavra.printLetters()
    
    def rodada(self):
        self.atualizar_interface()
        letra_escolhida = str(input("Escolha uma letra: ")).lower()
        while letra_escolhida.isalpha() == False:
            letra_escolhida = str(input("Letra inválida: ")).lower()
        if self.palavra.check(letra_escolhida) == False:
            self.erros += 1

        self.tentativas += 1



jogo1 = Game("elefante", lista_desenho)
