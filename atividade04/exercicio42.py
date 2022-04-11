# Exercício 42

numeroEntrada = 1
conjuntoA = 0 # 0-25
conjuntoB = 0 # 26-50
conjuntoC = 0 # 51-75
conjuntoD = 0 # 76-100

numeroEntrada = int(input("Entre com um número: "))

while(numeroEntrada >= 0):
    if numeroEntrada >=0 and numeroEntrada <= 25:
        conjuntoA +=1
    elif numeroEntrada >=26 and numeroEntrada <= 50:
        conjuntoB +=1
    elif numeroEntrada >=51 and numeroEntrada <= 75:
        conjuntoC +=1
    elif numeroEntrada >=76 and numeroEntrada <= 100:
        conjuntoD +=1
    numeroEntrada = int(input("Entre com um número: "))
    
print("Quantidade de números no intervalo [0-25]: ",conjuntoA)
print("Quantidade de números no intervalo [26-50]: ",conjuntoB)
print("Quantidade de números no intervalo [51-75]: ",conjuntoC)
print("Quantidade de números no intervalo [76-100]: ",conjuntoD)