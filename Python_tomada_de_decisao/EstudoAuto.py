a  = float(input("Digite o primeiro lado: "))

b  = float(input("Digite o segundo lado:"))

c = float(input("Digite o terceiro valor:"))

if ((a + b > c) and (a + c > b) and (b + c > a)):

    if(a == b == c):
        print("é um triângulo equilátero")
    
    elif((a == b) or (a == c) or (c == b)):
        print("É um triângulo isósceles")

    else:
        print("É um triângulo escaleno")

else:
    print("Não é um triângulo")