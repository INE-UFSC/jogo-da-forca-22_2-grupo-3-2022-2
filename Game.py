import string
from Checker import Checker
from desenhos import estagios_desenho_forca as lista_desenho

class Game():
    def __init__(self, palavra, estagios_desenho):
        self.palavra = Checker(palavra)
        
        self.tentativas = 0
        self.erros = 0
        self.limite_erros = len(estagios_desenho) 
        self.desenho_estagios = estagios_desenho # É possível utlizar diferentes desenhos de console no jogo. Para isso deve-se alterar o import
        self.vitoria = False
        self.finalizou = False
        self.letras_entradas = [] #esta informação está contida na classe Checker pelo método printLetters()
                                  #o qual printa as letras disponíveis com as letras que foram utilizadas já marcadas
    
    def run(self):
        running = True
        while running: #gameloop 
            pass

    def atualizar_interface(self):
        print("\nRodada atual: {}".format(self.tentativas))
        print(self.desenho_estagios[self.erros])
        self.palavra.printLetters()
    
    def rodada(self):
        self.atualizar_interface()
        letra_escolhida = str(input("Escolha uma letra: ")).lower()
        while self.palavra.check(letra_escolhida) == False:
            letra_escolhida = str(input("Letra inválida, escolha novamente: ")).lower()

        self.tentativas += 1

jogo1 = Game("ELEFANTE", lista_desenho)
jogo1.atualizar_interface()