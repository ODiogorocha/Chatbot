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