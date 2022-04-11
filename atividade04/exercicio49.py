# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

numeroEntrada = int(input("Entre com um número inteiro: ")) # N 
contador = 2
resultado = 1 # H
while(contador <= numeroEntrada):
    resultado += 1 / contador
    contador += 1
print(resultado)