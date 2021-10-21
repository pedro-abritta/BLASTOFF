def menorValor(a, b, c):
    menor = a;

    if b < a:
        menor = b
    if c < a:
        menor = c;
    return menor

a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))

print("O menor valor digitado é {} ".format(menorValor(a,b,c)))