bergamaschi = [1, 1, 1]


for i in range(3, 20):
    proximo_valor = bergamaschi[-1] + bergamaschi[-2] + bergamaschi[-3]
    bergamaschi.append(proximo_valor)

print(bergamaschi)