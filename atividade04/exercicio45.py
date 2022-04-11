# Exercício 45

continuar = "s"
quantidadeAlunos = 0
mediaTurma = 0
maiorAcerto = -1
menorAcerto = 11

while(continuar == "s" or continuar == "S"):
    acertos = 0
    for questao in range(10):
        numeroQuestao = questao + 1
        print("Entre com a alternativa escolhida da questão",numeroQuestao)
        resposta = input()
        if(numeroQuestao == 1 and (resposta == "A" or resposta == "a")):
            acertos += 1
        if(numeroQuestao == 2 and (resposta == "B" or resposta == "b")):
            acertos += 1
        if(numeroQuestao == 3 and (resposta == "C" or resposta == "c")):
            acertos += 1
        if(numeroQuestao == 4 and (resposta == "D" or resposta == "d")):
            acertos += 1
        if(numeroQuestao == 5 and (resposta == "E" or resposta == "e")):
            acertos += 1
        if(numeroQuestao == 6 and (resposta == "E" or resposta == "e")):
            acertos += 1
        if(numeroQuestao == 7 and (resposta == "D" or resposta == "d")):
            acertos += 1
        if(numeroQuestao == 8 and (resposta == "C" or resposta == "c")):
            acertos += 1
        if(numeroQuestao == 9 and (resposta == "B" or resposta == "b")):
            acertos += 1
        if(numeroQuestao == 10 and (resposta == "A" or resposta == "a")):
            acertos += 1

    if(acertos > maiorAcerto):
        maiorAcerto = acertos

    if(acertos < menorAcerto):
        menorAcerto = acertos

    quantidadeAlunos += 1
    mediaTurma += acertos
    
    continuar = input("Incluir respostas de um novo aluno ? S/N  ")
    
print("Maior acerto: ",maiorAcerto)
print("Menor acerto: ",menorAcerto)
print("Total de alunos que utilizaram o sistema: ", quantidadeAlunos)
print("Média geral da turma: ", mediaTurma / quantidadeAlunos)
