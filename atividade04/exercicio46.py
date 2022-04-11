# Exercício 46

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
