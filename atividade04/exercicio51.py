# Exercício 49/51

entradaNumero = int(input("Entre com o número: "))
numerosImpares = 1
contador = 1
resultado = 0

while(contador <= entradaNumero):
    resultado += contador/numerosImpares
    numerosImpares += 2
    contador += 1
print(resultado)
