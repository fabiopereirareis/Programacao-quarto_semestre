#Projeto interdisciplinar ADS 1/4B - 2022

def conversaoBases(entrada:int, base:int):
    """método que recebe um valor inteiro e um valor da base para conversão"""
    divisao = int(entrada / base)
    resto = entrada % base
    resultado = [resto]

    while (divisao > 0):
        resto = divisao % base
        divisao = int(divisao / base)
        resultado.append(resto)

    resultado.reverse()
    textoCompleto = ''

    if base == 16:
        textoCompleto = formatacaoHexadecimal(resultado)
    else:
        for numero in resultado:
            textoCompleto += str(numero)

    return textoCompleto

def formatacaoHexadecimal(vetor: int):
    """método que formata o valor de entrada com as letras usadas na base Hexadecimal"""
    textoCompleto = ''
    for elemento in vetor:
        if elemento >= 10:
            if elemento == 10:
                textoCompleto += 'A'
            if elemento == 11:
                textoCompleto += 'B'
            if elemento == 12:
                textoCompleto += 'C'
            if elemento == 13:
                textoCompleto += 'D'
            if elemento == 14:
                textoCompleto += 'E'
            if elemento == 15:
                textoCompleto += 'F'
        else:
            textoCompleto += str(elemento)
    return textoCompleto

def menuConversorBases():
    """Menu inicial com opções do conversor de bases"""

    print("*************")
    print("Seja bem vindo ao conversor de bases!")
    print("*************")

    opcao = int(0)
    
    while(opcao != 4):

        num = int(input("Digite um numero inteiro: "))

        print('''Escolha uma das bases para conversão:
        [1] Converter para BINÁRIO
        [2] Converter para OCTAL
        [3] Converter para HEXADECIMAL
        [4] SAIR''')

        opcao = int(input("Digite uma opção: "))

        if(opcao != 4):
            if(opcao == 1):
                resultado = conversaoBases(num,2)
            elif(opcao == 2):
                resultado = conversaoBases(num,8)
            elif(opcao == 3):
                resultado = conversaoBases(num,16)

            print("*************")
            print("Resultado: ",resultado)

menuConversorBases()

