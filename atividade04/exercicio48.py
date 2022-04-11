# Faça um programa que mostre os n termos da Série a seguir:

#       S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

#     Imprima no final a soma da série.

entradaNumero = int(input("Entre com o número: "))
numerosImpares = 1
contador = 1
resultado = 0

while(contador <= entradaNumero):
    resultado += contador/numerosImpares
    numerosImpares += 2
    contador += 1
print(resultado)

# solução 01
# entradaNUmero = int(input("Entre com o número: "))
# contadorImpar = 1
# contador = 1
# impares = 0
# resultado = 0
# while(contador < entradaNUmero):
#     if(contadorImpar % 2 != 0):
#         impares = contadorImpar
#     else:
#         contadorImpar += 1
#         impares = contadorImpar
#     resultado += contador/impares
#     contadorImpar += 1
#     contador += 1

# solução 02
# entradaNumero = int(input("Entre com o número: "))
# contadorImpar = 0
# contador = 1
# resultado = 0
# while(contador < entradaNumero):
#     if(contadorImpar % 2 == 0):
#         contadorImpar += 1
#     resultado += contador/contadorImpar
#     contadorImpar += 1
#     contador += 1