print("1 - Triângulo")
print("2 - Quadrado")
print("3 - Retângulo")
print("4 - Círculo")
print("5 - Fim de processo")
c = input("Escolha uma opção: ")



if  c == '1':
    altura = int(input("Digite a altura: "))
    base = int(input("Digite a base: "))
    triângulo = (altura * base) / 2
    print(f"O valor do triângulo é: {triângulo}") 

elif c == '2':
    lado = int(input("Digite o lado do quadrado: "))
    quadrado = lado * 2
    print(f"O valor do quadrado é: {quadrado}")

elif c == '3':
    compri = int(input("Digite o  valor do comprimento: "))
    largura = int(input("Digite o valor da largura: "))
    retan = compri * largura
    print(f"O valor do retângulo é: {retan}")

elif c == "4":
    raio = int(input("Digite o raio: "))
    circ = 3.14 * raio
    print(f"O valor da área do circulo é: {circ:.2f}") 

elif c == 5:
    print("O programa foi encerrado.")

else:
    print("Insira um valor válido")


    

    





