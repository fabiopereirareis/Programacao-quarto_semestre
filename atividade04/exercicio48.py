# Exercício 48

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


