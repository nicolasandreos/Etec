preço=float(input("Digite o preço do produto: "))
quantidade=int(input("Digite a quantidade do produto: "))
valordacompra= preço*quantidade

codigo=int(input("Digite o código do tipo do pagamento: "))

if codigo == 0:
    valorfinal= valordacompra-(25% valordacompra)
    print("O valor da compra é de R$",valordacompra,"o valor de desconto é de 25%, o valor final é de",valorfinal,"você escolheu o pagamento a vista.")
else:
    if codigo == 1:
        valorfinal= valordacompra-(20% valordacompra)
        print("O valor da compra é de R$",valordacompra,"o valor de desconto é de 20%, o valor final é de",valorfinal,"você escolheu o pagamento a cheque(30).")
    else:       
        if codigo == 2:
            valorfinal= valordacompra-(10% valordacompra)
            print("O valor da compra é de R$",valordacompra,"o valor de desconto é de 10%, o valor final é de",valorfinal,"você escolheu o pagamento cartão de crédito em 2 vezes.")
        else:     
            if codigo == 3:
                valorfinal= valordacompra-(5% valordacompra)
                print("O valor da compra é de R$",valordacompra,"o valor de desconto é de 5%, o valor final é de",valorfinal,"você escolheu o pagamento cartão de crédito em 3 vezes.")
            else:
                
                if codigo == 4:
                   print("O valor da compra é de R$",valordacompra,"o valor de desconto é de 0%,você escolheu o pagamento a vista.")
input("enter")
