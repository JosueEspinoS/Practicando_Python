#Operadores Básicos
'''Los operadores básicos en Python incluyen:
   +, -, *, /, //, % y ** 
'''
#Suma / Addition
#Resultado = 10
print("5+5 =",5+5)

#Resta / Subtraction
#Resultado = 2
print("5-3 =",5-3)

#Multiplicación
#Resultado = 50
print("5*10 =",5*10)

#División |el uso de "/" regresa un decimal|
#Resultado = 3.33333333
print("10/3 =",10/3)

#División de piso |(redondea hacia abajo la respuesta al número entero más cercano) regresa un int|
#Resultado = 3
print("10//3 =",10//3)

#Módulo |resto cuando  se divide |
#Resultado = 1
print("10%3 =",10%3)

#Exponente
print("2^1= ",2**1)
print("2^2= ",2**2)
print("2^3= ",2**3)

#M[as operadores de asignaci[on
# +=, -= y *=.
'''
Supongamos que tenemos la variable x, con un valor inicial de 10. Si queremos incrementar x en 2, podemos
escribir:
x = x + 2
El programa primero evaluará la expresión de la derecha (x + 2) y asignará la respuesta a la izquierda.
Entonces, eventualmente, la declaración anterior se convierte en x <- 12.

En lugar de escribir x = x + 2, también podemos escribir x += 2 para expresar el mismo significado. El signo
+= es en realidad una abreviatura que combina el signo de asignación con el operador de suma.

Por lo tanto, x += 2 simplemente significa x = x + 2.
'''
x=5
x = x+2 #Resultado 7
print(x)
#Utilizando la abreviatura
y = 5
y += 2 #Resultado 7
print(y)
#Funciona para los 7 operadores mencionados anteriormente.
#Ejemplo de Módulo
y %= 3 #Resultado 1
print(y)
