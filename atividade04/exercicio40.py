# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#     Código da cidade;
#     Número de veículos de passeio (em 1999);
#     Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#     Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#     Qual a média de veículos nas cinco cidades juntas;
#     Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

maiorIndice = -999999999
menorIndice = 999999999
cidadeMaiorIndice = ''
cidadeMenorIndice = ''
mediaVeiculos = 0
mediaAcidentes = 0
cidadesMenosVeiculos = 0

for cidade in range(5):
    
    codigoCidade = input("Código da cidade:")
    quantidadeVeiculos = int(input("Número de veículos de passeio:"))
    quantidadeAcidentes = int(input("Número de acidentes com vítimas:"))
    
    if quantidadeAcidentes > maiorIndice:
        maiorIndice = quantidadeAcidentes
        cidadeMaiorIndice = codigoCidade
    
    if quantidadeAcidentes < menorIndice:
        menorIndice = quantidadeAcidentes
        cidadeMenorIndice = codigoCidade

    mediaVeiculos += quantidadeVeiculos
    if quantidadeVeiculos < 2000:
        mediaAcidentes += quantidadeAcidentes
        cidadesMenosVeiculos += 1
    print('')

print('Menor indice de acidentes, cidade:',cidadeMenorIndice,',',menorIndice,'acidentes')
print('Maior indice de acidentes, cidade:',cidadeMaiorIndice,',',maiorIndice,'acidentes')
print('Média de veículos', mediaVeiculos / 5)
print('Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio',int(mediaAcidentes/cidadesMenosVeiculos))