def area_cuadrado(lado):
    area = (lado ** 2) 
    return print(f"el área de su cuadrado es {area}")
area_cuadrado(4) 
"""
esta funcion funciona proporcionando un lado del cuadrado
calculamos el área con su formula  con el dato del lado 
y retornamos un print con el resultado del area 
"""

def mayor_de_tres(a, b, c):
    if a > b and a > c:
        print(f"{a} es  mayor a {b} y {c}")
    elif b > c:
        print(f"{b} es  mayor a {a} y {c}")
    else:
        print(f"{c} es  mayor a {a} y {b}")

mayor_de_tres(9, 4, 5)
"""
esta función funciona proporcionando 3 datos 
primero una condicion if para saber si a es mayor a los demás
segundo otra condicion si b es mayoe a c
y un else porque ya solo queda que c sea el número mayor 

"""
numeros = input("Escriba tres números: ")
lista_numeros = []
lista_numeros.append(numeros)
print(lista_numeros)
while numeros != "fin":
