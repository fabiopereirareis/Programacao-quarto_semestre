# Exercício 41

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
    
    print("{:.2f}".format(dividaComJuros),"        ","{:.2f}".format(valorJuros),"        ",parcela,"                   ","{:.2f}".format(valorParcela))

    parcela += 3
    

   

