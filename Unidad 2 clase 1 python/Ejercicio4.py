#Desarrollar un programa que solicite al usuario los lados de un rectángulo y calcule su
#perímetro y su superficie.
#Informar ambos resultados por pantalla.

print ("Por favor, ingrese la medida del lado horizontal")
horizontal= float(input())
print ("Por favor, ingrese la medida del lado vertical")
vertical= float(input())
perimetro= (horizontal*2)+(vertical*2)
print ("El perimetro es {}".format(perimetro))
superficie= (horizontal*vertical)
print ("la superficie es {}".format(superficie))

