#Lista
'''
La lista se refiere a una colección de datos que normalmente están relacionados. En lugar de almacenar estos
datos como variables separadas, podemos almacenarlos como una lista.

Para declarar una lista, escribe listName = [valores iniciales]. Tenga en cuenta que usamos corchetes [ ]
cuando declaramos una lista. Los valores múltiples están separados por una coma.

'''

frutas=['manzana','mango','uvas']

numeros=[1,2,3,4,5,6,7,8,9]

listaVacia=[]

#método append() para agregar elementos  al final de lista
listaVacia.append('Blanco') #0 index
listaVacia.append('Gris')   #1
listaVacia.append('Negro')  #2
listaVacia.append('Azul')   #3
listaVacia.append('Verde')  #4
listaVacia.append('Rojo')   #5
listaVacia.append('Morado') #6

'''
La notación 2:4 se conoce como rebanada. Siempre que usamos la notación de corte en Python, el elemento del
índice de inicio siempre se incluye, pero el elemento del final siempre se excluye. Por lo tanto, la notación 2:4 se
refiere a elementos del índice 2 al índice 4-1 (es decir, índice 3)
'''

print(listaVacia)       #Mostrar todos los elementos de la lista
print(listaVacia[2])    #imprimir un elemento especifico
print(listaVacia[-1])   #imprimir ultimo elemento de una lista [-1]
print(listaVacia[1:3])  #mostrar elemento desde 1 a 2 sin mostrar el 3
print(listaVacia[1:])   #mostrar elementos desde 1 hasta el ultimo -1
print(listaVacia[:4])   #imprimir desde 0 hasta 3 sin mostrar el 4
listaVacia2 = listaVacia[1:5:2] # un tercer número conocido como paso a paso. Si escribimos listaVacia2 =listaVacia[1:5:2], obtendremos una sublista que consiste en cada segundo número del índice 1 al
print(listaVacia2)

listaRandom=[1,2,'hello']
print(listaRandom)
listaRandom += frutas   #Unir  2 listas
print("----____listaRandom += frutas----____")
print(listaRandom)
#modificar elemento especifico de una lista
listaRandom[3]='World!'
print(listaRandom)      #Cambio "manzana" por "World!"
listaRandom.pop(-1)     #ejemplo Elimina ultimo elemento de lista, se especifica el index a eliminar
print(listaRandom)
listaRandom.append(66)
listaRandom.append(67)
listaRandom.append(69)
listaRandom.append(68)
listaRandom.append(69)
print(listaRandom)

listaRandom.remove(69)  #remove() elimina el primer elemento encontrado con el valor coincidente en una lista dada
print(listaRandom)