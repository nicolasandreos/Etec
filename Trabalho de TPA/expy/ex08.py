preço=input("Digite o preço do produto: ")
quantidade=int(input("Digite a quantidade do produto: "))

valordacompra= preço*quantidade

codigo=input("Digite o codigo do pagamento")

if codigo > 0:
    if codigo > 1:
        if codigo > 2:
            if codigo > 3:
                valorfinal=valordacompra
                desconto=0
            else:
                valorfinal1= 5% valordacompra
                desconto1=5
        else:
            valorfinal2=10% valordacompra
            desconto2=10
    else:
        valorfinal3= 20% valordacompra
        desconto3=20
else:
    valorfinal4=25% valordacompra
    desconto4=25
    
print("O valor da compra é de R$",valordacompra,"com desconto de",desconto,", totalizando",valorfinal)

input("enter")
