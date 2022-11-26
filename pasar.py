# AVANZADOS

#Ejercicio 1:
#a) Defina una función que reciba como argumento una cadena de texto y retorne un
#valor entero indicando la cantidad de vocales que contiene la cadena Ejemplo:
#“agua” -> 3, “pepe” ->2
#b) Defina una función que genere una lista de palabras hasta que se ingrese la
#palabra “fin” la cual NO debe ser almacenada en la lista, por cada palabra,
#también se guardara la cantidad de vocales que contiene la misma, para esto
#deberá utilizar la función definida en el punto 1) a, al finalizar la función deberá
#retornar la lista generada.
#a) La lista resultado deberá tener una estructura similar a:
#1) [[“uno”,2],[ “pepe”,2],[”agua!”,3],…etc]
#c) defina una función que reciba como argumento la lista generada en el punto 1.b) e
#imprimir las palabras que tienen mas de 3 vocales.
#d) escriba el código del programa que integra las 3 funciones antes definidas.

#def vocales(pal):
#	voc = 0
#	letras = "aeiou"
#	for x in pal:
#		if x in letras:
#			voc = voc + 1
#	return pal,voc

#def palabras():
#	lista = []
#	vocc = 0
#	tot = 0
#	pala = input("ingrese una palabra o fin: ")
#	while pala != "fin":
#		for x in pala:
#			if x in "aeiou":
#				vocc = vocc + 1
#		j = [pala,vocc]
#		lista.append(j)
#		vocc = tot
#		pala = input("ingrese una palabra o fin: ")
#	return lista

#def conteo(palabritas):
#	for x in palabritas:
#		if x[1] >= 3:
#			print(x[0])
	
#palabritas = palabras()
#pal = input("ingresar una palabra: ")
#print(vocales(pal))
#print(palabritas)		
#conteo(palabritas)
			

#Ejercicio 2:
#resuelva modularizando
#a) Realice un programa para manejar equipos de fútbol, Armar una lista que tenga
#información sobre los equipos de fútbol. Para cada equipo deberán tener: el
#nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor.
#b) Usando la lista anterior, imprimir la cantidad de goles a favor que tienen los
#equipos que están en la primera y última posición de la lista.
#c) Imprimir el nombre del equipo Campeón de la lista generada en el punto a), el
#equipo campeón es aquel que sumo más puntos.

#def equipos():
#	lista1 = []
#	equipo = input("ingrese nombre del equipo o fin: ")
#	while equipo != "fin":
#		punt = int(input("ingrese puntaje: "))
#		goles = int(input("ingrese la cantidad de goles: "))
#		dato = [equipo,punt,goles]
#		lista1.append(dato)
#		equipo = input("ingrese nombre del equipo o fin: ")
#	return lista1

#def goles(equipito):
#	aux1 = 0
#	for x in equipito:
#		if aux1 < x[2]:
#			aux1 = x[2]
#	print("el primero en lista con sus goles a favor es: ", aux1)

#def campeon(equipito):
#	sumi = 0
#	for j in equipito:
#		if sumi < j[1]:
#			sumi = j[1]
#	print(sumi)

#equipito = equipos()
#goles(equipito)
#campeon(equipito)

#Ejercicio 3:
#Implemente los siguientes puntos:
#a) Realice una función que procesa la información de alumnos de la UNAJ. De cada
#alumno se conoce legajo, nombre, apellido, contraseña. El procesamiento termina
#cuando se ingresa el número de legajo 0. La función deberá retornar una lista con
#la información procesada.

#def alumnos():
#	lista1 = []
#	legajo = int(input("ingrese su legajo o 0: "))
#	while legajo != 0:
#		nombre = input("ingrese su nombre: ")
#		apellido = input("ingrese su apellido: ")
#		contra = input("ingrese su contraseña: ")
#		data = [legajo,nombre,apellido,contra]
#		lista1.append(data)
#		legajo = int(input("ingrese su legajo o 0: "))
#	return lista1


#b) Realice una función llamada imprimir_alumno que recibe como parámetro una lista
#con los datos de un alumno (Legajo, nombre, apellido, contraseña), los datos del
#alumno serán mostrados por pantalla con la forma:
#Legajo:XXXX
#Nombre:XXXX
#Apellido:XXXX
#Contraseña:XXXXX

#def imprimir_alumno(data_alumnos):
#	for x in data_alumnos:
#		print("Legajo: ",x[0])
#		print("Nombre: ",x[1])
#		print("Apellido: ",x[2])
#		print("Contraseña: ",x[3])	


#c) Realice un función llamada legajo_menor que recibe como parámetro una lista de
#alumnos, de cada alumno se conoce la información (legajo, nombre, apellido,
#contraseña), la función debe buscar cuál es el alumno con el menor legajo dentro
#de la lista y retornarlo.

#def legajo_menor(data_alumnos):
#	men = 9999999
#	for i in data_alumnos:
#		if i[0] < men:
#			men = i[0]
#	print("el legajo menor es")
#	return men



#d) Realice un función llamada nombre_mas_largo que recibe como parámetro una
#lista de alumnos. La función debe buscar cuál es el alumno con el nombre más
#largo dentro de la lista y retornarlo.

#def nombre_mas_largo(data_alumnos):
#	may = 0
#	for h in data_alumnos:
#		if len(h[1]) > may:
#			may = len(h[1])
#			print("el nombre mas largo es: ",h[1])
#	return may
	

#e) Realice un función llamada controlar_clave que recibe como parámetro un
#alumno,(legajo, nombre, apellido, contraseña). La función debe controlar si la
#contraseña es mayor a 6 caracteres y termina con un número, deberá imprimir un
#mensaje especificando el error cometido en caso de no cumplir las condiciones o
#bien imprimir los datos del alumno si la clave cumple con todas las condiciones.

#def controlar_clave(data_alumnos):
#	num = ("0","1","2","3","4","5","6","7","8","9")
#	for k in data_alumnos:
#		if (len(k[3]) > 6) and (k[3][-1] in num):
#			print("los datos estan correctos")
#			print(k)
  

#Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir
#del menú, el resto de las opciones permiten :
#- imprimir los datos de todos los alumnos con el formato pedido en el punto a)
#- imprimir los datos del alumno que tiene el legajo más chico.
#- imprimir los datos del alumno que tiene el nombre más largo.
#- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6
#caracteres y terminan con un número.



#menu = "n1/ datos -- n2/ legajo mas chico -- n3/ nombre mas largo -- n4/ contraseña bien"
#print(menu)
#op = int(input("ingrese una opcion o 5 para salir: "))
#while op != 5:
#	if op == 1:
#		data_alumnos = alumnos()
#		print(data_alumnos)
#	elif op == 2:
#		print(legajo_menor(data_alumnos))
#	elif op == 3:
#		print(nombre_mas_largo(data_alumnos))
#	elif op == 4:
#		controlar_clave(data_alumnos)
#	else:
#		print("opcion incorrecta")
#		print(menu)
#	op = int(input("ingrese una opcion o 5 para salir: "))
		

#Ejercicio 4:
#Se desea realizar un programa para una universidad. El mismo deberá permitir guardar la
#información de todos los cursos que se dictan en la misma. La cantidad de cursos
#existentes es ingresado por el usuario del sistema. De cada curso se debe conocer:
#Nombre, Cantidad de Clases, Día de Dictado, Hora de Comienzo, Duración en minutos.
#Importante: si la duración del curso es mayor a 360 minutos, NO se debe guardar la
#información del mismo.
#El programa debe permitir
#a) Imprimir todos los cursos que tengan más de 5 clases
#b) Imprimir los cursos que se dictan en un día de la semana indicado por el usuario.
#c) Imprimir el curso más intensivo (definido por la cantidad de clases y la duración de
#cada clase)
#d) Imprimir los datos en que se dicta un curso indicado por el usuario.
#e) Imprima todos los cursos que comienzan con una letra indicada por el usuario.
#El programa escrito deberá mostrar un menú para que el usuario elija la opción deseada.
#Importante: el sistema termina cuando el usuario elige la opción “salir”.

#def cursos():
#	lista = []
#	nombre = input("ingresar nombre del curso: ")
#	while nombre != "fin":
#		cant = int(input("ingrese la cantidad de clases: "))
#		dia = input("ingrese dia de dictado: ")
#		hora = int(input("ingrese hora de comienzo: "))
#		dura = int(input("ingrese duracion en minutos: "))
#		data = [nombre,cant,dia,hora,dura]
#		if dura < 360:
#			lista.append(data)
#		nombre = input("ingresar nombre del curso: ")
#	return lista

#a) Imprimir todos los cursos que tengan más de 5 clases

#def curso_cantidad(curso_data):
#	for x in curso_data:
#		if x[1] >= 5:
#			print(x)
	
#b) Imprimir los cursos que se dictan en un día de la semana indicado por el usuario.
#def clase_dia(curso_data):
#	didi = input("ingrese el dia que desea y se mostraran las clases: ")
#	for j in curso_data:
#		if didi == j[2]:
#			print("ese dia estan los cursos: ",j)

#c) Imprimir el curso más intensivo (definido por la cantidad de clases y la duración de
#cada clase)

#def intenso(curso_data):
#	ca = 0
#	dur = 0
#	for h in curso_data:
#		if h[1] > ca:
#			ca = h[1]
#	print("el curso con mas cantidad de clases es: ",h)
#		if h[4] > dur:
#			dur = h[4]
#	print("el curso con mas duracion de clases es: ",h)

#d) Imprimir los datos en que se dicta un curso indicado por el usuario.
#def curso_usu(curso_data):
#	dat = input("ingrese materia y se mostraran sus datos: ")
#	for l in curso_data:
#		if dat == l[0]:
#			print(l)

#e) Imprima todos los cursos que comienzan con una letra indicada por el usuario.
#def letra(curso_data):
#	le = input("ingrese letra y se mostrara los cursos correspondientes: ")
#	for k in curso_data:
#		if le == k[0][0]:
#			print("el curso con la inicial es: ",k)


#El programa escrito deberá mostrar un menú para que el usuario elija la opción deseada.
#Importante: el sistema termina cuando el usuario elige la opción “salir”.
#def menu():
#	op = int(input("ingrese opcion: "))
#	while op != 7:
#		if op == 1:
#			print(curso_data)
#		elif op == 2:
#			curso_cantidad(curso_data)
#		elif op == 3:
#			clase_dia(curso_data)
#		elif op == 4:
#			intenso(curso_data)
#		elif op == 5:
#			curso_usu(curso_data)
#		elif op == 6:
#			letra(curso_data)
#		else:
#			print("incorrecto")
#		op = int(input("ingrese opcion: "))

#curso_data = cursos() 
#menuu = "n1/sus datos ingresados. n2/filtro de cursos menores. n3/ curso por dia. n4/ curso intenso. n5/ curso por nombre. n6/ curso por letra. n7/ salir"
#print(menuu)
#menu()


#Ejercicio 5:
#Nos contratan para realizar un sistema para un kiosco. De cada artículo se conoce
#código, nombre, una descripción, el precio de venta, el nombre del proveedor y si es
#necesaria la refrigeración del artículo (pudiendo ser R=requiere frío o N=no requiere frío).
#a) Realice una función que cree una lista con información de artículos de kiosco. La
#carga de artículos finaliza cuando se ingresa un artículo cuyo código = “999” y que
#a la vez no requiera frío.

#def kiosco():
#	lista1 = []
#	codigo = input("ingrese codigo: ")
#	refri = input("ingrese R si requiere frio o N si no requiere: ")
#	while codigo != "999" and refri != "n":
#		nombre = input("ingrese nombre del producto: ") 
#		desc = input("ingrese descripcion: ")
#		precio = int(input("ingrese el precio: "))
#		prov = input("ingrese el nombre del proveedor: ")
#		data = [codigo,refri,nombre,desc,precio,prov]
#		lista1.append(data)
#		codigo = int(input("ingrese codigo: "))
#		refri = input("ingrese R si requiere frio o N si no requiere: ")
#	return lista1


#b) Realice una función que cree una lista con los datos del stock, donde de cada
#articulo se conoce el código y la cantidad existente.

#def stock(kiosco_data):
#	lista2 = []
#	for x in kiosco_data:
#		print("ingrese cantidad de stock de: ",x[2])
#		cant = int(input("cantidad: "))
#		data_stock = [x[2], x[0],cant]
#		lista2.append(data_stock)
#	return lista2
	

#c) Se requiere imprimir los datos de todos los artículos que necesitan refrigeración o
#los artículos que no la necesitan, dependiendo del valor ingresado por el usuario
#(R=requiere frío o N=no requiere frío).

#def refri(kiosco_data):
#	for k in kiosco_data:
#		if k[1] == "r":
#			print("requiere frio: ",k)
#		elif k[1] == "n":
#			print("no requiere frio",k)


#kiosco_data = kiosco()
#print(kiosco_data)
#print(stock(kiosco_data))
#refri(kiosco_data)

#d) Se necesita imprimir la cantidad de artículos que necesitan refrigeración y la
#cantidad de artículos que no la necesitan.
#e) Se requiere imprimir los datos de los artículos cuyo stock es 0, de la siguiente
#manera: Código, nombre del artículo, y nombre del proveedor.
#f) Realice una función que utilizando la lista de productos creada en a) y en b)
#genere una nueva lista con la información completa de los artículos que no
#requieren frío, indicando además la cantidad existente.
#Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir
#del menú, el resto de las opciones permiten:
#- imprimir los datos de los artículos que necesitan o no refrigeración, dependiendo
#del valor ingresado por el usuario
#- imprimir la cantidad de artículos que precisan refrigeración
#- imprimir la cantidad de artículos que no requieren refrigeración
#- imprimir los datos de los artículos cuyo stock es 0
#- imprimir la información completa de los artículos que no requieren frío.

#def datas():
	#lista1 = []
#	codigo = int(input("ingrese codigo: "))
#	while codigo != -1:
	#	nombre = input("ingrese nombre del producto: ")
		#cant = int(input("ingrese cantidad de producto: "))
#		precio = int(input("ingrese el precio: "))
#		datita = [codigo,nombre,cant,precio]
#		lista1.append(datita)
#		codigo = int(input("ingrese codigo: "))
#	return lista1

#def porcentaje(lista_data):
#	cont = 0
#	for x in lista_data:
#		if x[2] < 10:
#			cont = cont + 1
#	tot = (cont * 100)
#	print("el porcentaje es: ",tot /len(lista_data))

#def menor(lista_data):
#	cont = 999999
#	for j in lista_data:
#		if j[3] < cont:
#			cont = j[3]
#			nom = j[1]
#	return cont,nom
	
#def menu(lista_data):
#	menuu = "op1/ datos ingresados. op2/ porcentajes. op3/ menor precio. op4/ salir"
#	print(menuu)
#	op = int(input("ingrese opcion: "))
#	while op != 4:
#		if op == 1:
#			print(lista_data)
#		if op == 2:
#			print(porcentaje(lista_data))
#		if op == 3:
#			print(menor(lista_data))
#	else:
#		print(menuu)
#	op = int(input("ingrese opcion: "))
	
		
#lista_data = datas()
#menu(lista_data)
