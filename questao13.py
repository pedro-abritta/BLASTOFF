matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input("Digite um valor: "))

for c in range(0, 3):
    for l in range(0, 3):
        print("[{}]".format(matriz[c][l]), end="")
    print()