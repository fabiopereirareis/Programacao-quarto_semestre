# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

#     1 , 2, 3, 4  - Votos para os respectivos candidatos 
#     (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#     5 - Voto Nulo
#     6 - Voto em Branco

#     Faça um programa que calcule e mostre:
#     O total de votos para cada candidato;
#     O total de votos nulos;
#     O total de votos em branco;
#     A percentagem de votos nulos sobre o total de votos;
#     A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

candidato01 = 0
candidato02 = 0
candidato03 = 0
candidato04 = 0
nulo = 0
branco = 0

opcao = 7


while(opcao != 0):
    print("Opção 1 jose | Opção 2 Maria | Opção 3 Jõao | Opção 4 Helena")
    print("Opção 5 Nulo | Opção 6 Branco | Opção 0 **SAIR**")
    opcao = int(input("Entre com uma opção: "))
    if(opcao == 1):
        candidato01 += 1
    elif(opcao == 2):
        candidato02 += 1
    elif(opcao == 3):
        candidato03 += 1
    elif(opcao == 4):
        candidato04 += 1
    elif(opcao == 5):
        nulo += 1
    elif(opcao == 6):
        branco += 1

totalVotos = candidato01 + candidato02 + candidato03 + candidato04 + nulo + branco
porcentagemNulos = (nulo * 100) /totalVotos
porcentagemBrancos = (branco * 100) /totalVotos
print("Total de votos do candito 1 jose = ", candidato01)
print("Total de votos do candito 2 Maria = ", candidato02)
print("Total de votos do candito 3 Jõao = ", candidato03)
print("Total de votos do candito 4 Helena = ", candidato04)
print("Total de votos nulos = ", nulo)
print("Total de votos brancos = ", branco)
print("Percentual de votos nulos = {:.2f}".format(porcentagemNulos))
print("Percentual de votos brancos = {:.2f}".format(porcentagemBrancos))


    
    