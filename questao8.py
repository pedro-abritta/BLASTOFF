num = int(input("Digite um valor: "))

valor = 1
cont = 0

while valor <= num:
    if num % valor == 0:
        cont = cont + 1
    valor = valor +1
if cont > 2:
    print("o numero {} NÃO é primo".format(num))
else:
    print("o numero {} é primo".format(num))