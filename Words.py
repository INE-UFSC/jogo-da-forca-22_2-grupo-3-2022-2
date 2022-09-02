import requests
import json

class Words():
    def __init__(self):
        pass

    def get_random_word(self):
        
        #utilizar uma api para coletar uma palavra
        r = requests.get('https://api.dicionario-aberto.net/random')
        obj = json.loads(r.text)
        
        if r.status_code == 200: return obj['word']
        else : return ""


if __name__ == '__main__':
    w = Words()
    print(w.get_random_word())