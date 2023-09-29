x = int(input("Digite um valor positivo: "))

while(x <= 0):
    print("Erro!")
    x = int(input("Digite um valor positivo: "))

a = int(input("Digite o primeiro valor limitante: "))
b = int(input("Digite o segundo valor limitante (sendo maior que o primeiro): "))

while(b <= a):
    print("Erro!")
    b = int(input("Digite o segundo valor limitante (sendo maior que o primeiro): "))

for i in range (b, a -1, -1):
    r = x * i
    print(f"{x} x {i} = {r}")