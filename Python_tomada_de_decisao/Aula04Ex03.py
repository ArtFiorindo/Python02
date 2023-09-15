valor1 = float(input("Digite o primeiro valor: "))

valor2 = float(input("Digite o segundo valor: "))

valor3 = float(input("Digite o terceiro valor: "))

if (valor1 > valor2):
    if (valor1 > valor3):
        print("O valor 1 é o maior!")
    else:
        print("O valor 3 é o maior!")

else:
    if (valor2 > valor3):
        print("O valor 2 é o maior!")
    else:
        print("O valor 3 é o maior!")