print('Ola qual o seu nome ?')
nome = input('>: ')

if 'O meu nome e ' in nome:
	nome = nome[14:]
else:
	print(f'Muito prazer {nome}')

while True:
	resposta = input('>: ')
	if resposta == 'tchau':
		break
	else:
		print("digite outra coisa ")