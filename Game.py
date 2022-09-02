class Game():
    def __init__(self, palavra):
        self.palavra = [*palavra.upper()]
        
        self.erros = 0
        self.tentativas = 0
        self.vitoria = False
        self.finalizou = False
        self.letras_entradas = []
        self.letras_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    