fibonacci = [1, 1]

for i in range(2, 30):
    proximo_valor = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_valor)


print(fibonacci)