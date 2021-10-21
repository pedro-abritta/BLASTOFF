while True:
    a = int(input("Digite a hora em que a partida começou: "))
    b = int(input("Digite a hora em que a partida terminou: "))
    if a < b:
        break;

tempo = b - a;

print("O tempo gasto de partida foi de {}h".format(tempo))