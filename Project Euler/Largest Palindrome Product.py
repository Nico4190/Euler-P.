
n = int(input("Ingrese el valor del n-digito que deseas: "))

def largest_palindrome_product():

    max_palindrome = 0

    for i in range(10**(n-1), 10**n):

        for j in range(i, 10**n):

            product = i * j

            if str(product) == str(product)[::-1] and product > max_palindrome:

                max_palindrome = product

    return max_palindrome
print(largest_palindrome_product())