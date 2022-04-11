# Exercício 50

numeroEntrada = int(input("Entre com um número inteiro: ")) # N 
contador = 2
resultado = 1 # H
while(contador <= numeroEntrada):
    resultado += 1 / contador
    contador += 1
print(resultado)