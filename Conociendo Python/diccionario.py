#Diccionario 
'''
es una colección de pares de datos relacionados. Por ejemplo, si queremos almacenar el nombre de
usuario y la edad de 5 usuarios, podemos almacenarlos en un diccionario.

Para declarar un diccionario, escribe dictionaryName = {dictionary key: data}, con el requisito de que las claves
del diccionario deben ser únicas (dentro de un diccionario). Es decir, no puede declarar un diccionario como este
myDictionary = {“Peter”:38, “John”:51, “Peter”:13}.

'''
#dictionaryName = {dictionary key: data}
#Crear diccionario
users={
    "Juan":45,
    "Pepe":25,
    "Mariana":45,

}
print(users)

persona={
    'nombre':'juan',
    'edad':25

}
print(persona)

diccionarioVacio={ #Crear diciconario vacio

}
print(diccionarioVacio) #imprimir todo el diccionario
diccionarioVacio['German']=40 #Agregar un elemento al diccionario
diccionarioVacio['Arely']=20
print(diccionarioVacio)
diccionarioVacio['Arely']='No disponible' #editar un elemento utilizando la key
print(diccionarioVacio)
print(diccionarioVacio['Arely']) #acceder a dato por medio de la key (key: data)
print(diccionarioVacio['German'])