#Los factores principales de son y.¿Cuál es el factor primo más grande del número?

n = int(input("Ingrese un numero: "))

def largest_prime_factor(n):

    factor = 2

    while factor * factor <= n:

        if n % factor == 0: 

            n //= factor
        else:
            factor += 1

    return n

print(largest_prime_factor(n))



