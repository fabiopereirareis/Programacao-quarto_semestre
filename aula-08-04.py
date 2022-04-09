# método for
#entradaNumero = int(input("Digite um número inteiro: ")) # 10
#for numero in range(11): # 0,1,2,3,4,5,6,7,8,9,10
                         # 1,2,3,4,5,6,7,8,9,10,11
     #print("%d x %d = %d" %(entradaNumero, numero, entradaNumero*numero))
    #print(entradaNumero, " vezes ", numero, " = ", entradaNumero*numero)
#    print(entradaNumero*numero)

# ****************************************************************************
# método while
#resposta = "s"
#rodadas = 0
#soma = 0

#while(resposta == "s" or resposta == "S"):
#    numero = float(input("Entre com um número: "))
#    soma += numero
#    rodadas += 1
#    resposta = input("Deseja continuar? S/N \n")
#media = soma / rodadas
#print("O valor da média é,",media)

# ****************************************************************************
# **** binário
entrada = int(input("Digite um número inteiro:"))

binario = ""
while entrada!=0:
    resto = entrada%2
    binario = str(resto) + binario
    entrada = entrada//2
print(binario)