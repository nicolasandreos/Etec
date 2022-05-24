nota=float(input("Digite os pontos obtidos na prova: "))

if  (nota>=0) and(nota<=100):
    if nota > 30:
        if nota > 60:
           if nota > 90:
               print("Ótimo")
           else:
              print("Muito bom")
        else:
          print("Bom")
    else:
       print("Regular")
else:
    print("Pontuação inválida")
    
input("enter")