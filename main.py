from chatbot import Chatbot

Bot = Chatbot("Jarves")

print("     _________                            ")
print("    / ======= \\                          ")
print("   / __________\\                         ")
print("  | ___________ |                         ")
print("  | | -       | |                         ")
print("  | |         | |                         ")
print("  | |_________| |________________________ ")
print("  \\=____________/   JARVES     )")
print("  / \"\"\"\"\"\"\"\"\"\"\" \\                       / ")
print(" / ::::::::::::: \\                  =D-'  ")
print("(_________________)                     ")

while True:
    frase = Bot.escuta()
    resp = Bot.pensar(frase)
    Bot.fala(resp)
    if frase.lower() == 'tchau':
        break
    else:
        print("Digite outra coisa ou diga 'tchau' para sair.")
