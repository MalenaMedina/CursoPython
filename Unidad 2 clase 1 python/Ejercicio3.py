#Solicitar por teclado el ingreso de un número entero.
#Asignar dicho número a una variable, transformarla a coma flotante y mostrarla por
#pantalla (valor y tipo de variable).


print ("Por favor, ingresar un numero entero")
ingreso= int(input())
ingresoConComa= float(ingreso)
print ("ingreso Con Coma={}".format(ingresoConComa))
print ("tipo de variable={}".format(type(ingresoConComa)))

