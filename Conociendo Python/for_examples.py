'''
a = (1, 5, 8, 4, 5)
sum_x = 10
for i in a:
    sum_x += i print sum_x
'''

#1.- Realice un programa que enumere los paises de la siguiente lista
#paises = ['Canada', 'USA', 'Mexico', 'Australia']

def paisesEnumerados():
    ciudades = ['Canada', 'USA', 'Mexico', 'Australia','Brasil', 'Japon']
    print('Ciudades enumeradas:')
    lugar=0
    for x in ciudades:
        lugar+=1
        print('Ciudad: #' + str(lugar)+'- ' + x)

#2.- Crear un ciclo for que cuente de 0 a 100
def cero100():
    for x in range (0,101):
        print(x)


#3.- Tabla de multiplicar
def multiplicar():
    num1 = [1,2,3,4,5,6,7,8,9,10]
    factor = 9

    for x in num1:
        producto= x*factor
        print(str(x)+ '*' + str(factor)+ '=' + str(producto))
        
#4.- Imprima los números del 1 a 10 al revés utilizando el ciclo for
def alreves():
    for x in range (10,0,-1):
        print(x)
#4.1- Otra forma 
def alreves2():
    for x in reversed(range(1,11,1)):
        print(x)
        
#4.2- Imprima los números del 1 a 10 al utilizando el ciclo for
def derecho():
    for y in range (1,11):
        print(y)

#5.- Crear un bucle que cuente todos los números pares hasta el 100
def pares():
    numPar=0
    for x in range(0,101,2):
        numPar+=1
        print('número= '+str(x)+ '| ID par: '+ str(numPar))#Imprime todos los numeros pares iniicando desde 0
    print('Total Números Pares:'+ str(numPar-1))# se resta -1 por que inicia desde 0, entonces cuenta a 0 como par
#5.1 .- otra forma
def pares2():
    numPar=0
    for x in range(0,101):
        if (x%2==0):
            numPar+=1
    print('Pares: '+ str(numPar-1))
            
#6.- Cree un bucle que sume los números del 100 al 200
def suma200():
    suma=0
    for x in range(100,201):
        print('número a sumar :' + str(x))#imprimiendo número a sumar
        suma+=x
        print('Suma parcial= ' +str(suma))#imprimiendo suma parial 
        print('_._._sumando_._._')
    print('Total:'+str(suma))
#7.- Dado un número, cuente el número total de dígitos de un número
    #Por ejemplo, el número es 75869, por lo que la salida debería ser 5.
def lenNum(numero):
    longitud=0
    for x in str(numero):
        longitud+=1
    print(longitud)
#7.1.- Otra forma sin For
def lenNum2(numero):
    print(len(str(numero)))
        
#8.- Mostrar series de Fibonacci hasta 10 términos
def fibFor():
    for x in range(10):
        print(fib(x))
#8.1.- Otra manera sin For
def fib(n):
    if n< 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

#9.- Use un bucle para mostrar elementos de una lista dada que estén presentes en posiciones pares
def paresEnLista():
    frutas =['manzana','mango','uvas','banana','sandia','guayaba']
    num1=0
    for x in frutas:
        if (num1%2 ==0):
            print(x)
        num1+=1
#10.- Imprima el siguiente patrón con el ciclo for:
    '''
*
**
***
****
*****
****
***
**
*
'''
def patronPyra():
    sizePyra=5   
    for x in range(0,sizePyra):    
        for y in range(0,x+1):
            print("*",end='')
        print("\r")
        
    for x in reversed(range(0,sizePyra-1)):    
        for y in reversed(range(0,x+1)):
            print("*",end='')
        print("\r")
# imprime el siguiente patron
'''
*
**
***
****
*****
'''
def mediaPyra():
    sizePyra=5   
    for x in range(0,sizePyra):        
        for y in range(0,x+1):
            print("*",end='')
        print("\r")

# imprime el siguiente patron
'''
54321
4321
321
21
1
'''
def patronNumeros():
    num=5   
    for x in reversed(range(1,num+1)):
        for y in reversed(range(1,x+1)):
            print(y,end='')
        print("\r")

#cree un bucle que diga si es  numero primo 
def numPrimo(k):
    
    if k > 1:
        for i in range(2, int(k/2)+1):
             if (k % i) == 0:
                print("No es número Primo")
                break
        else:
            print("Es Número Primo")

    else:
        print("No es número Primo")
