# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

#     Exemplo:

#       12376489
#       => 98467321

numeroEntrada = int(input("Entre com um número inteiro positivo: "))

conversao = str(numeroEntrada)
stringVetor = []
stringSaida = ''

for letra in conversao:
    stringVetor.append(letra)

stringVetor.reverse()

for letra in stringVetor:
    stringSaida += letra

print(stringSaida)


