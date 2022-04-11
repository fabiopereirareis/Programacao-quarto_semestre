# Exercício 47

nomeAtleta = ''
nomeAtleta = input("Entre como nome do atleta: ")

contador = 0
melhorNota = -1.0
piorNota = 11.0
media = 0.0
notas = []

while(contador <7):
    print("Entre com a nota: ",contador+1)
    nota = float(input())
    notas.append(nota)
    contador += 1
    if(nota < piorNota):
        piorNota = nota
    if(nota > melhorNota):
        melhorNota = nota
print("***********************")
print("Atleta: ",nomeAtleta)
contagemNotas = 1

for nota in notas:
    print("Nota:", contagemNotas, ",", nota)
    contagemNotas += 1
    if(nota != melhorNota and nota != piorNota):
        media += nota

print("***********************")
print("Resultado final")
print("Atleta: ",nomeAtleta)
print("Melhor nota: ",melhorNota)
print("Pior nota: ",piorNota)
media /= 5
print("Média {:.2f}".format(media))
print()

