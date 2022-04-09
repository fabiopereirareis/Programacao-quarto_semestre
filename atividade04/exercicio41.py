# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

#     Os juros e a quantidade de parcelas seguem a tabela abaixo:

#     Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#     1       0
#     3       10
#     6       15
#     9       20
#     12      25

#     Exemplo de saída do programa:

#     Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#     R$ 1.000,00     0               1                       R$  1.000,00
#     R$ 1.100,00     100             3                       R$    366,00
#     R$ 1.150,00     150             6                       R$    191,67

from decimal import getcontext
from numpy import double

valorDivida = double(input("Entre com o valor da dívida R$:"))
parcelaMaxima = 12
parcela = 1
juros = 0

# print(valorDivida,"|",juros,"|",parcela,"|",valorDivida+juros)
print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
print("{:.2f}".format(valorDivida),"        ","{:.2f}".format(juros),"          ",parcela,"                    ","{:.2f}".format(valorDivida+juros))
parcela += 2
while(parcela <= parcelaMaxima):
    if parcela == 3:
        juros = 0.10
    if parcela == 6:
        juros = 0.15
    if parcela == 9:
        juros = 0.20 
    if parcela == 12:
        juros = 0.25
    
    valorJuros = valorDivida * juros
    dividaComJuros = valorDivida + valorJuros
    valorParcela = dividaComJuros / parcela
    # print(dividaComJuros,"|",valorJuros,"|",parcela,"|",valorParcela)
    print("{:.2f}".format(dividaComJuros),"        ","{:.2f}".format(valorJuros),"        ",parcela,"                   ","{:.2f}".format(valorParcela))

    parcela += 3
    

   

