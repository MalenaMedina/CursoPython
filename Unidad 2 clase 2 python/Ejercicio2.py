#Escribir un programa que pida ingresar un número entero mayor que cero por teclado.
#Verificar si el número ingresado es múltiplo de 2, 3, 4, 5, 6, 7,8 o 9.
#Armar una lista con los números encontrados (por ejemplo, si el número ingresado es
#múltiplo de 3,6 y 7, armamos una lista que contenga estos tres números).
#Mostrar la lista por pantalla, ordenada de mayor a menor.
#En caso de que el número ingresado no sea múltiplo de estos números, mostrar por
#pantalla el mensaje “No se encontraron divisores exactos

ListaDeMultiplos = []

listNumero = [2,3,4,5,6,7,8,9]
print ("Por favor, ingrese un numero Mayor que 0")
numeroUsuario = int(input())
if numeroUsuario < 0: print("Error. Por favor, ingrese un numero mayor a 0")
for numero in listNumero:
    if numeroUsuario % numero == 0:
        ListaDeMultiplos.insert(0,numero)        
largoDeLista = len(ListaDeMultiplos)
if largoDeLista > 0:
    print (ListaDeMultiplos)
else:
    print ("No se encontraron divisores exactos")
