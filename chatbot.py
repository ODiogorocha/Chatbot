import json

class Chatbot:
    def __init__(self, nome):
        memoria = open('nome+.json','r')
        self.historico = []

    def escuta(self):
        frase = input('>: ')
        return frase.strip().lower().title()

    def pensar(self, frase):
        if frase.lower() == "oi":
            resposta = 'Olá! Qual o seu nome?'
        elif self.historico and self.historico[-1] == 'Olá! Qual o seu nome?':
            nome = pega_o_nome(frase)
            resposta = responde_o_nome(nome)
        elif frase.lower() == 'tchau':
            resposta = 'Tchau! Até mais :)'
        else:
            resposta = 'Não entendi.'
        return resposta
import json

# FUNÇÕES
def resposta():
    resposta = input('>: ')
    resposta = resposta.lower().title()
    return resposta

def pega_o_nome(nome):
    if 'Meu Nome Eh' in nome:
        novo_nome = nome[14:]
    else:
        novo_nome = nome
    return novo_nome

def responde_o_nome(nome):
    nomes_conhecidos = ['Raimundo', 'Joao', 'Diogo']

    if nome in nomes_conhecidos:
        frase = 'Eaew '
    else:
        frase = 'Muito prazer '
    return frase + nome

# CLASSE CHATBOT
class Chatbot:
    def __init__(self, nome):
        try:
            with open(f'{nome}.json', 'r') as memoria:
                self.dados = json.load(memoria)
        except FileNotFoundError:
            self.dados = {}
        self.historico = []

    def escuta(self):
        frase = input('>: ')
        return frase.strip().lower().title()

    def pensar(self, frase):
        if frase.lower() == "oi":
            resposta = 'Olá! Qual o seu nome?'
        elif self.historico and self.historico[-1] == 'Olá! Qual o seu nome?':
            nome = pega_o_nome(frase)
            resposta = responde_o_nome(nome)
        elif frase.lower() == 'tchau':
            resposta = 'Tchau! Até mais :)'
        else:
            resposta = 'Não entendi.'
        return resposta

    def fala(self, frase):
        print(frase)
        self.historico.append(frase)
