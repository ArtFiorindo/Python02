a = float(input("Digite o valor da aceleração em (m/s2): "))
b = float(input("Digite o valor da velocidade inicial em (m/s): "))
c = float(input("Digite o tempo de percurso em (s): "))

v = (b + (a * c)) * 3.6

print(f"A velocidade final foi:{v:.2f} Km/h")

if (v <= 40):
    print("Veiculo muito lento")
    
elif (v <= 60):
        print("Velocidade permitida")
    
elif (v <= 80):
        print("Velocidade de cruzeiro")
    
elif (v <= 120):
        print("Veículo rápido")

else:
    print("Veículo muito rápido")
