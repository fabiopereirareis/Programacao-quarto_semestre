# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m

from unittest import result


nomeAtleta = ''
nomeAtleta = input("Entre como nome do atleta: ")
resultadoFinal = []
while(nomeAtleta != ''):
    contador = 0
    melhorSalto = -1.0
    piorSalto = 30.0
    media = 0.0
    saltos = []
    melhores = []

    while(contador <5):
        print("Entre com o salto número:",contador+1)
        salto = float(input())
        saltos.append(salto)
        contador += 1
        if(salto < piorSalto):
            piorSalto = salto
        if(salto > melhorSalto):
            melhorSalto = salto
    print("***********************")
    print("Atleta: ",nomeAtleta)
    contagemSaltos = 1

    for salto in saltos:
        print("Salto número:", contagemSaltos, ",", salto, "m")
        contagemSaltos += 1
        if(salto != melhorSalto and salto != piorSalto):
            media += salto

    print("***********************")
    print("Melhor salto: ",melhorSalto, "m")
    print("Pior salto: ",piorSalto, "m")
    media /= 3
    print("Média {:.2f} m".format(media))
    print()
    # print("Resultado final")
    # # print(nomeAtleta, ":{:.2f}".format(media))
    resultadoFinal.append(str(nomeAtleta + ":{:.2f} m".format(media)))
    nomeAtleta = input("Entre como nome do atleta: ")

print("***********************")
print("Resultado final")
# resultado = str(nomeAtleta + ":{:.2f}".format(media))
for resultado in resultadoFinal:
    print(resultado)
