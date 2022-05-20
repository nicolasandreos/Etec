salario=float(input("Informe o seu salário: "))
prestaçao_carne=float(input("Digite a prestação da carne a ser pago: "))

salario_20= 20% salario
if prestaçao_carne > salario_20:
    print("Empréstimo não pode ser concedido.")
    
else:
    print("Empréstimo pode ser concedido.")
    
input("enter")
