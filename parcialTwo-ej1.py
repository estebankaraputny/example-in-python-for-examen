# a) Defina una función que reciba como argumento una cadena de texto y retorne un
# valor entero indicando la cantidad de vocales que contiene la cadena Ejemplo:
# “agua” -> 3, “pepe” ->2

# b) Defina una función que genere una lista de palabras hasta que se ingrese la
# palabra “fin” la cual NO debe ser almacenada en la lista, por cada palabra,
# también se guardara la cantidad de vocales que contiene la misma, para esto
# deberá utilizar la función definida en el punto 1) a, al finalizar la función deberá
# retornar la lista generada.
# a) La lista resultado deberá tener una estructura similar a:
# 1) [[“uno”,2],[ “pepe”,2],[”agua!”,3],…etc]

# c) defina una función que reciba como argumento la lista generada en el punto 1.b) e
# imprimir las palabras que tienen mas de 3 vocales.

# d) escriba el código del programa que integra las 3 funciones antes definidas.

def vocales(pal):
	voc = 0
	letras = "aeiou"
	for x in pal:
		if x in letras:
			voc = voc + 1
	return pal,voc

def palabras():
	lista = []
	vocc = 0
	tot = 0
	pala = input("ingrese una palabra o fin: ")
	while pala != "fin":
		for x in pala:
			if x in "aeiou":
				vocc = vocc + 1
		j = [pala,vocc]
		lista.append(j)
		vocc = tot
		pala = input("ingrese una palabra o fin: ")
	return lista

def conteo(palabritas):
	for x in palabritas:
		if x[1] >= 3:
			print(x[0])
	
palabritas = palabras()
pal = input("ingresar una palabra: ")
print(vocales(pal))
print(palabritas)		
conteo(palabritas)

