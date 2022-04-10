
codigo100 = 1.20
codigo101 = 1.30
codigo102 = 1.50
codigo103 = 1.20
codigo104 = 1.30
codigo105 = 1.00

quantidade100 = 0
quantidade101 = 0
quantidade102 = 0
quantidade103 = 0
quantidade104 = 0
quantidade105 = 0

subtotal100 = 0
subtotal101 = 0
subtotal102 = 0
subtotal103 = 0
subtotal104 = 0
subtotal105 = 0

pedido = "n"

while(pedido == "N" or pedido == "n"):
    codigoProduto = int(input("Entre com o código do produto: "))
    quantidadeProduto = int(input("Entre com a quantidade do produto: "))
    if(codigoProduto == 100):
        subtotal100 += (quantidadeProduto * codigo100)
        quantidade100 += quantidadeProduto
        
    elif(codigoProduto == 101):
        subtotal101 += (quantidadeProduto * codigo101)
        quantidade101 += quantidadeProduto

    elif(codigoProduto == 102):
        subtotal102 += (quantidadeProduto * codigo102)
        quantidade102 += quantidadeProduto

    elif(codigoProduto == 103):
        subtotal103 += (quantidadeProduto * codigo103)
        quantidade103 += quantidadeProduto

    elif(codigoProduto == 104):
        subtotal104 += (quantidadeProduto * codigo104)
        quantidade104 += quantidadeProduto

    elif(codigoProduto == 105):
        subtotal105 += (quantidadeProduto * codigo105)
        quantidade105 += quantidadeProduto
    
    print("Deseja fechar o pedido?")
    pedido = input("S / N: ")
print("Subtotal:")
print("Especificação   Código  Preço")
print("Cachorro Quente 100     R$ 1,20 x ",quantidade100," = {:.2f}".format(subtotal100))
print("Bauru Simples   101     R$ 1,30 x ",quantidade101," = {:.2f}".format(subtotal101))
print("Bauru com ovo   102     R$ 1,50 x ",quantidade102," = {:.2f}".format(subtotal102))
print("Hambúrguer      103     R$ 1,20 x ",quantidade103," = {:.2f}".format(subtotal103))
print("Cheeseburguer   104     R$ 1,30 x ",quantidade104," = {:.2f}".format(subtotal104))
print("Refrigerante    105     R$ 1,00 x ",quantidade105," = {:.2f}".format(subtotal105))
print("Total do pedido: {:.2f}".format(subtotal100+subtotal101+subtotal102+subtotal103+subtotal104+subtotal105))