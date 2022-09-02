from Checker import Checker
from desenhos import estagios_desenho_forca as lista_desenho


class Game():
    def __init__(self, palavra, estagios_desenho = lista_desenho):
        self.palavra = Checker(palavra)

        self.rodada_atual = 0
        self.erros = 0
        self.limite_erros = len(estagios_desenho)
        self.desenho_estagios = estagios_desenho  # É possível utlizar diferentes desenhos de console no jogo. Para isso deve-se alterar o import
        self.letras_entradas = []  # Lista das letras inseridas pelo usuário, usada para impedir que seja possível inserir letras já escolhidas

    def run(self):
        running = True
        while running:  # gameloop
            self.rodada()
            if self.fim_de_jogo():
                if self.jogo_ganho():
                    print("\nParabéns você ganhou!")
                    break
                else:
                    print("\nVocê perdeu.")
                    print("Palavra correta: {}".format(self.palavra.getWord().upper()))
                    break

    def rodada(self):
        self.atualizar_interface()

        letra_escolhida = str(input("Escolha uma letra: ")).upper()
        # Restrições de entrada
        while (letra_escolhida.isalpha() == False) or (len(letra_escolhida) != 1) or (letra_escolhida in self.letras_entradas):
            letra_escolhida = str(input("Letra inválida, digite novamente: ")).upper()
        
        # Se a letra escolhida foi aceita, será colocada na lista de letras já escolhidas
        self.letras_entradas.append(letra_escolhida)
        
        if self.palavra.check(letra_escolhida) == False:
            self.erros += 1

        self.rodada_atual += 1
    
    def atualizar_interface(self):
        print("\nRodada atual: {}".format(self.rodada_atual))
        print(self.desenho_estagios[self.erros])
        print(f"Número de erros permitidos: {self.limite_erros - self.erros}")
        print(self.palavra.getSuccessfullWord())
        self.palavra.printLetters()

    def fim_de_jogo(self):
        return self.jogo_ganho() or self.erros == self.limite_erros

    def jogo_ganho(self):
        if '_' not in self.palavra.getSuccessfullWord():
            return True
        else:
            return False


if __name__ == "__main__":
    jogo1 = Game("elefante")
    jogo1.run()