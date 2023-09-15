altura = float(input("Digite a sua altura: "))

peso =float(input("Digite a o seu peso: "))

imc = peso / (altura * altura)

if (imc < 20):
    print("Você está abaixo do peso!")

elif (imc < 25):
    print("Você está com peso ideal!")

else:
    print("você está acima do peso ideal!")