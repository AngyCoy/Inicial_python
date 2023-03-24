#operaciones solo con resultados  true or false ()
#OPERACIONES RELACIONALES O DE COMPARACION < >
number = int(input("Digite un número mayor a 5: "))

print(number > 5)  #mayor a 5
print(number >= 5)  #mayor o igual a 5
print(number == 5)  #igual a 5
print(number != 5)  #no igual a 5

#OPERACIONES LOGICAS
print("operaciones logicas ")
#conjunción AND/SI (&)
print(False and False)
print((number >= 5) & True)
print((number >= 3) & (number <= 8))
#DISYUCCIÓN OR/O (|)
print(False or False)
print(True | False)
print(True or True)
print(False | True)

#NEGACIÓN not ~
print(not (True))
print(not (False))

#EXCLUSIVA ^
print(False ^ False)
print(True ^ False)
print(True ^ True)
print(False ^ True)
print((number >= 3) ^ (number <= 8))

#OPERACIONES DE PERTENENCIA  "in"

nombre = "Angy"
print("A" in nombre)
