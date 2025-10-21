import math 

def esprimo(n):
    if n <2: 
        return False
    if n == 2 or n == 3:
        return True
    if n%2 == 0: 
        return False 
    
    limite = int(math.sqrt(n)) +1 

    for i in range(3, limite, 2): 
        if n % i == 0: 
            
            return False
    return True





numero = int(input('Ingrese un numero ', ))
primos = set()

n=2 

while len(primos)< numero: 
    if esprimo(n):
        primos.add(n)
    n+=1
print(f"El numero primo {numero} es: {sorted(primos)[numero-1]}")


