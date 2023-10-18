#Pedirle al usuario que ingrese dos números enteros por teclado y contar cuantos números
#pares hay entre ambos valores ingresados.
#Ingresar primer numero: 3
#ingresar segundo numero: 98
#entre 3 y 98 se encontraron: 48 numeros pares

print ("Por favor, ingrese dos numeros enteros")
numeroUno=  int(input("numero 1: "))
numeroDos= int(input ("numero 2: "))
totalNumeros= list(range(numeroUno,numeroDos+1))
countNumPares = 0
for numerosPares in totalNumeros:
    if numerosPares %2 == 0:
        countNumPares= countNumPares + 1 
print ("entre {} y {} se encontraron: {}".format (numeroUno,numeroDos,countNumPares))

