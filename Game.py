import string
from Checker import Checker
from desenhos import estagios_desenho_forca as lista_desenho

class Game():
    def __init__(self, palavra, estagios_desenho):
        self.palavra = [*palavra.upper()]
        
        self.erros = 0
        self.limite_erros = len(estagios_desenho) 
        self.desenho_estagios = estagios_desenho # É possível utlizar diferentes desenhos de console no jogo. Para isso deve-se alterar o import
        self.tentativas = 0
        self.vitoria = False
        self.finalizou = False
        self.letras_entradas = []
        self.letras_alfabeto = string.ascii_uppercase
    
    def atualizar_interface(self):
        print(self.desenho_estagios[self.erros])


jogo1 = Game("ELEFANTE", lista_desenho)
jogo1.atualizar_interface()
    