
def sumsquare(n): 
        suma = 0
        for i in range(n+1): 
            suma += i*i
        return suma

def squaresum(n): 
      suma = 0
      for i in range(n+1): 
            suma+= i 
      return suma*suma
      
def rest(n):
      a = squaresum(n) - sumsquare(n)
      return a



usuario = int(input('Ingrese un numero ', ))
print(squaresum(usuario))
print(sumsquare(usuario))
print(rest(usuario))


