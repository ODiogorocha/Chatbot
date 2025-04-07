import json
from funcoes import pega_o_nome, responde_o_nome

class Chatbot:
    def __init__(self, nome):
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
