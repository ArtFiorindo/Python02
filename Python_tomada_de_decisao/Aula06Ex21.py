a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))


print("1 - Multiplição")
print("2 - Adição")
print("3 - Divisão")
print("4 - Subtração")
print("5 - Fim do programa")

c = input("Escolha uma opção: ")


if c == '1':
    resultado = a * b
    print(f"O resultado em multiplição: {resultado}")

elif c == '2':
    resultado2 = a + b
    print(f"O resultado da adição: {resultado2}")

elif c == '3':
    if (b != 0):
        resultado3 = a / b
        print(f"O resultado da divisão: {resulatdo3}")

elif c == '4':
    resultado4 = a - b
    print(f"O resultado da subtração foi: {resultado4}")

elif c == '5':
    print("Programa Encerrado")
    breakpoint
    

else:
    print("Opção inválida. Por favor escolha uma opção válida.")

    