palavra = input("Digite uma palavra: ")

if str(palavra) == "".join(reversed(palavra)) :
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")