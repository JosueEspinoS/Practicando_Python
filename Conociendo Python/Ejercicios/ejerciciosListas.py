#1.- Cuál de las opciones nos permite obtener 
# una lista con los siguientes valores : [9,16,25]
#lista original: lst_num = [3,4,5]

lst_num = [3,4,5]
'''for n in lst_num:
    print(n**2)
'''
output = [n ** 2 for n in lst_num]
print(output)
# 2. Completa la linea de código faltante para obtener los textos en mayúscula
# a partir de la siguiente lista:
lst_lp = ["python", "c", "java","php"]

'''for lp in lst_lp:
    print(lp.upper())
'''
output2=[lp.upper() for lp in lst_lp]
print(output2)

#3.- ¿Qué elementos tendrá la lista al ejecutar el siguiente código?
num=[1,2,3,4]
out=[n-1 for n in num if n<=3]
print(out)

#4. ¿Cuál de las opciones nos permite obtener una lista 
# con los siguientes elementos: [2, 3, 3, 4]?

lst_num2 = [1, 2, 3, 4]
output3=[n + 1 if n <= 2 else n for n in lst_num2]
print(output3)

#5. ¿Cuál de las opciones nos permite obtener una lista
#  con los siguientes elementos: ['P', 'P', ‘H’]?.

letras_1 = ['P','Y','T', 'H','O', 'N']
letras_2 = ['P','H','P']
output4 = [a for a in letras_1 for b in letras_2 if a == b]
print(output4)

#Checando Mutable Inmutable
num1=2
num2=3
suma = num1+num2
print(id(suma))
suma=30
print(id(suma))
x=True
print(id(x))
x=False
print(id(x))