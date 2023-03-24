#operaciones aritmeticas suma + resta- multi*
#divi con decimal/ divi exacta // residuo%, potencia**

number = int(input("Digite un número mayor a 5: "))
print(f"La suma del número más 3 es: {number+3}")
print(f"La resta del número menos 2 es: {number-2}")
print(f"La multiplicación del número por 4 es: {number*4}")
print(f"La división del número entre 2 es: {number/2}")
print(f"La división EXACTA del número entre 2 es: {number//2}")
print(f"El residuo al dividir el número entre 3 es: {number%3}")
print(f"La potenciación del número elevado al cubo es: {number**3}")

#OPERACIONES DE ASIGNACIÓN
#+= incremental -= decremental

number += 1
print(f"Al usar operador incremental += el resultado es:  {number}")
number -= 1
print(f"Después de usar el operador decremental, el resultado es {number}")
number *=2
print(f"Al usar el operador *=, el resultado es:  {number}")
number /=2
print(f"Al usar el operador /= entre 2, el resultado es:  {number}")
number //=2
print(f"Al usar el operador //=, el resultado es:  {number}")
number **=2
print(f"Al usar el operador **=, el resultado es:  {number}")
number %=2
print(f"Al usar el operador %=, el resultado es:  {number}")