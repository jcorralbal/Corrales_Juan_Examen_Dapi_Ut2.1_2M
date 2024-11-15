numero_ent =int(input("Escriba un numero entero positivo: "))
if numero_ent % 2 == 0:
    print(f"{numero_ent} es par")
else:
    print(f"{numero_ent} es impar")

numero_nuevo =int(input("Escriba un numero entero positivo: "))
lista = []
for i in range (3, numero_nuevo + 1):
    if i % 3 == 0:
        lista.append(i)
print(f"Los múltiplos de 3 hasta {numero_nuevo} son {lista}")
