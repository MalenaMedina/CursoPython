#Escribir un programa que permita al usuario ingresar por teclado tantos números enteros
#como desee. Cuando no quiera ingresar más números, deberá ingresar el cero.
#A continuación, determinar cuál de los números ingresados es el mayor y cuál es el menor.
#Mostrar ambos por pantalla.


numMin = 9999999999999
numMax = 0
numIngresados = int(input("Ingrese tantos numeros enteros como desee. Cuando no desee ingresar más inserte 0:  "))
while numIngresados != 0:
    if numIngresados > numMax:
        numMax = numIngresados
    if numIngresados < numMin:
        numMin = numIngresados
    numIngresados = int(input("Ingrese tantos numeros enteros como desee. Cuando no desee ingresar más inserte 0:  "))
print ("El nùmero Mayor es {} y el numero minimo es {}".format(numMax, numMin))


    

