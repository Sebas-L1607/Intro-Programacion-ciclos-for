"""
Calcular el factorial de un numero

El factorial de un numero se define como 
fact(n) = 1 x 2 x 3 x 4 x 5 x 6... x n; 0! = 1

"""

numero = int(input("Ingrese el valor de n: "))

if numero == 0: 
    print (1)

elif numero > 0:
    fact = 1
    for num in range (1,numero+1):
        fact = fact * num
    print (numero, "! = ",fact)

else: 
    print("Error, n debe ser mayor o igual a 0")