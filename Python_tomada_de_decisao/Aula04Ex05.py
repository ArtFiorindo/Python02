lado1 = float(input("Digite o valor do primeiro lado: "))

lado2 = float(input("Digite o valor do segundo lado: "))

lado3 = float(input("Digite o valor do terceiro lado: "))

if ((lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)):
    
    if ((lado1 == lado2 ==lado3)):
        print("é um triângulo equilátero")
    
    elif ((lado1 == lado2) or (lado1 == lado3)or(lado2 == lado3)):
        print("É um triângulo isósceles")
    
    else:
        print("É um trângulo escaleno")

else:
    print("Não é possível formar um triângulo")
    



