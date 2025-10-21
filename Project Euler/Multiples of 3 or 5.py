
def multiplosde3e5(n):

    suma = 0
    for i in range(n):

        if i % 3 == 0 or i % 5 == 0:
            suma += i

    return suma

input_usuario = int(input("Ingrese un numero: "))
print(multiplosde3e5(input_usuario))