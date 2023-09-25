#Si creamos tres listas. La primera contiene 4 números, la segunda contiene 5 letras y en la
#tercera le cargamos como elementos las dos listas anteriores.
#¿Cuántos elementos contendrá la tercera lista? Demostrar mediante un breve código.

lista1= list(range(1,5))
lista2= ["a","b","c","d","e"]
lista3= lista1 + lista2
print (len(lista3))


