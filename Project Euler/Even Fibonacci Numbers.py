
n = int(input("Ingrese un numero: "))
def even_fibonacci_numbers():

    a, b = 1, 2

    total = 0

    while a < n :

        if a % 2 == 1:
            
            total += a

        a, b = b, a + b

    return total

print(even_fibonacci_numbers())  