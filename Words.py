import requests
import json

class Words():
    '''A classe Words implementa o método getRandomWord, que retorna uma string com uma palavra aleatória retirada da api dicionario-aberto.net'''
    def __init__(self) -> None:
        pass

    def getRandomWord(self) -> str:
        
        #utilizar uma api para coletar uma palavra
        r = requests.get('https://api.dicionario-aberto.net/random')
        obj = json.loads(r.text)
        
        if r.status_code == 200: return obj['word']
        else : return ""

if __name__ == '__main__':
    w = Words()
    print(w.get_random_word())