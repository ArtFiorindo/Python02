sexo = input("Digite o sexo (F/M): ").upper()  

while ((sexo != "F") and (sexo != "M")):
    print("Resposta inválida. Por favor, digite 'F' para feminino ou 'M' para masculino.")
    sexo = input("Digite o sexo (F/M): ").upper()

print("Correto!")