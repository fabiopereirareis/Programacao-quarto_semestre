# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

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

