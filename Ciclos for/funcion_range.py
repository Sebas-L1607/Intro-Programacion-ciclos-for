"""
Sintaxis de Range (): 

range (Inicio, fin, paso)

- El inicio por default es 0, si no se indica lo contrario. 
- El paso por defaults es 1, si no se indica lo contrario. 
- El fin es OBLIGATORIO definirlo

- La funcion range() genera una serie de numeros enteros entre 
el inicio y el fin -1, con incremento dado por el paso

"""

#caso 1: range(fin)
# En este caso el inicio por defecto es 0 y por defecto el incremento es de 1 en 1.

print (list(range(10))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. 
print (list(range(101))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.... 100

# caso 2: range(inicio, fin) 

print(list(range(1,32)))
print(list(range(11,13)))

# caso 3: range (inicio, fin, paso)

print(list(range(3,20,2)))
print(list(range(0,123,3)))
print(list(range(-4,30,2)))
print(list(range(55,4,-5)))
