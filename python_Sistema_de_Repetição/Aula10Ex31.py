maior_valor = float('-inf')  
soma = 0

for i in range(1, 11):
    while True:
        try:
            valor = float(input(f"Digite o valor positivo #{i}: "))
            if valor >= 0:
                break
            else:
                print("Valor inválido. Insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

    # Atualize o maior valor e some o valor inserido
    if valor > maior_valor:
        maior_valor = valor
    soma += valor

media = soma / 10


print(f"O maior valor é: {maior_valor}")
print(f"A soma dos valores é: {soma}")
print(f"A média aritmética dos valores é: {media}")