from chatbot import Chatbot

Bot = Chatbot("diogo")
while True:
    frase = Bot.escuta()
    resp = Bot.pensar(frase)
    Bot.fala(resp)
    if resp.lower() == 'tchau':
        break
    else:
        print("Digite outra coisa ou diga 'tchau' para sair.")
