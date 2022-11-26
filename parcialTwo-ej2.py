# a) Realice un programa para manejar equipos de fútbol, Armar una lista que tenga
# información sobre los equipos de fútbol. Para cada equipo deberán tener: el
# nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor.
# b) Usando la lista anterior, imprimir la cantidad de goles a favor que tienen los
# equipos que están en la primera y última posición de la lista.
# c) Imprimir el nombre del equipo Campeón de la lista generada en el punto a), el
# equipo campeón es aquel que sumo más puntos.


def equipos():
	lista1 = []
	equipo = input("ingrese nombre del equipo o fin: ")
	while equipo != "fin":
		punt = int(input("ingrese puntaje: "))
		goles = int(input("ingrese la cantidad de goles: "))
		dato = [equipo,punt,goles]
		lista1.append(dato)
		equipo = input("ingrese nombre del equipo o fin: ")
	return lista1

def goles(equipito):
	aux1 = 0
	for x in equipito:
		if aux1 < x[2]:
			aux1 = x[2]
	print("el primero en lista con sus goles a favor es: ", aux1)

def campeon(equipito):
	sumi = 0
	for j in equipito:
		if sumi < j[1]:
			sumi = j[1]
	print(sumi)

equipito = equipos()
goles(equipito)
campeon(equipito)

