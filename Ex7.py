a = float(input("Valor primeiro produto: "))
b = float(input("Valor segundo produto: "))
c = float(input("Valor terceiro produto: "))
d = float(input("Valor quarto produto: "))
e = float(input("Valor quinto produto: "))

Pagamento = float(input("Valor do Pagamento: "))

s = a + b + c + d + e 

t = Pagamento - s

print(f"Valor do Troco {t:.2f}")