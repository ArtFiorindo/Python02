while True:
    try:
        N = int(input("Digite a quantidade de valores (N): "))
        if 0 < N < 20:
            break
        else:
            print("Quantidade inválida. Deve ser um valor positivo menor que 20.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro válido.")


maior_valor = float('-inf')  # Inicialize com o menor valor possível
menor_valor = float('inf')  # Inicialize com o maior valor possível
soma = 0
valores_positivos = 0
valores_negativos = 0


for i in range(1, N + 1):
    while True:
        try:
            valor = float(input(f"Digite o valor #{i}: "))
            break
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

    if valor > maior_valor:
        maior_valor = valor

    if valor < menor_valor:
        menor_valor = valor

    soma += valor

    if valor > 0:
        valores_positivos += 1
    elif valor < 0:
        valores_negativos += 1


media = soma / N


porcentagem_positivos = (valores_positivos / N) * 100
porcentagem_negativos = (valores_negativos / N) * 100


print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")
print(f"A soma dos valores é: {soma}")
print(f"A média aritmética dos valores é: {media:.2f}")
print(f"A porcentagem de valores positivos é: {porcentagem_positivos:.2f}%")
print(f"A porcentagem de valores negativos é: {porcentagem_negativos:.2f}%")