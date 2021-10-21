num = int(input("Digite um número: "))

fat = 1
i = 2

while i <= num:
    fat = fat * i
    i = i + 1
print("O fatorial de {} é: {}".format(num, fat))