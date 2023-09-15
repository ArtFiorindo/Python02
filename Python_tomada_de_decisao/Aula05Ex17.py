a = float(input("Digite a sua altura: "))
b = float(input("Digite o seu peso: "))
c = input("Digite o seu sexo (M/F): ")

imc = b / (a*a)


    
if(c.upper == 'M'):  
    if (imc < 20):
        print("Você está abaxio do peso.")
    elif(imc < 25):
        print("Você está com o peso ideal")
    else:
        print("Você está acima do peso")

elif(c.upper == 'F'):  
    if(imc < 19):
        print("Você está acima do peso")
    elif(imc < 24):
        print("Você está com peso ideal")
    else:
        print("Você está acima do peso")

else:
    print("Sexo inválido")
