# Exercício 44

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


    
    