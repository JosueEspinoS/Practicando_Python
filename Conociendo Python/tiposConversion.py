#Tipo de conversion
#int()
'''
Hay tres funciones integradas en Python que nos permiten realizar conversiones de tipos. Estas son las
funciones int(), float() y str().
La función int() en Python toma un flotante o una cadena apropiada y la convierte en un número entero.
Para cambiar un flotante a un entero, podemos escribir int(5.712987). Obtendremos 5 como resultado
(cualquier cosa después de quitar el punto decimal). Para cambiar una cadena a un número entero,
podemos escribir int ("4") y obtendremos 4. Sin embargo, no podemos escribir int ("Hola") o int ("4.22321").
Obtendremos un error en ambos casos.
'''
print(int(50.38)) # resultado 50
print(int("30")) # resultado 30
#print(int("20.23")) no se puede convedrtir un string flotante a integer

#float()
'''
La función float() toma un número entero o una cadena apropiada y lo cambia a un flotante. Por ejemplo, si
escribimos float(2) o float(“2”), obtendremos 2.0. Si escribimos float(“2.09109”), obtendremos 2.09109 que es
un float y no una cadena ya que se eliminan las comillas.
'''
print(float(2))
print(float("43.2423"))

#str()
'''
La función str(), por otro lado, convierte un número entero o un flotante en una cadena. Por ejemplo, si
escribimos str(2.1), obtendremos "2.1".
'''
print(str(2.1))
print(str(27))

#Utilizar el método type() para saber que tipo de dato es
print(type(str(27)))
print(type(int(50.38)))
print(type(float(2)))


