#Solicitar por teclado la cantidad de partidos ganados, empatados y perdidos de un
#determinado club de fútbol. Calcular y mostrar el puntaje final sabiendo que cada partido
#ganado le otorga 3 puntos, cada partido empatado 1 punto y ningún punto por cada
#partido perdido

partidoGanado= 3
partidoEmpatado= 1
partidoPerdido= 0
print ("cuantos partidos ganados hubo?")
ganados= int(input())
print ("cuantos partidos empatados hubo?")
empatados= int(input())
print ("cuantos partidos perdidos hubo?")
perdido= int(input())
puntajeFinal= (ganados*partidoGanado)+(empatados*partidoEmpatado)
print (puntajeFinal)
