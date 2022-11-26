
#Ejercicio 3:
#Implemente los siguientes puntos:
#a) Realice una función que procesa la información de alumnos de la UNAJ. De cada
#alumno se conoce legajo, nombre, apellido, contraseña. El procesamiento termina
#cuando se ingresa el número de legajo 0. La función deberá retornar una lista con
#la información procesada.

def alumnos():
	lista1 = []
	legajo = int(input("ingrese su legajo o 0: "))
	while legajo != 0:
		nombre = input("ingrese su nombre: ")
		apellido = input("ingrese su apellido: ")
		contra = input("ingrese su contraseña: ")
		data = [legajo,nombre,apellido,contra]
		lista1.append(data)
		legajo = int(input("ingrese su legajo o 0: "))
	return lista1


#b) Realice una función llamada imprimir_alumno que recibe como parámetro una lista
#con los datos de un alumno (Legajo, nombre, apellido, contraseña), los datos del
#alumno serán mostrados por pantalla con la forma:
#Legajo:XXXX
#Nombre:XXXX
#Apellido:XXXX
#Contraseña:XXXXX

def imprimir_alumno(data_alumnos):
	for x in data_alumnos:
		print("Legajo: ",x[0])
		print("Nombre: ",x[1])
		print("Apellido: ",x[2])
		print("Contraseña: ",x[3])	


#c) Realice un función llamada legajo_menor que recibe como parámetro una lista de
#alumnos, de cada alumno se conoce la información (legajo, nombre, apellido,
#contraseña), la función debe buscar cuál es el alumno con el menor legajo dentro
#de la lista y retornarlo.

def legajo_menor(data_alumnos):
	men = 9999999
	for i in data_alumnos:
		if i[0] < men:
			men = i[0]
	print("el legajo menor es")
	return men



#d) Realice un función llamada nombre_mas_largo que recibe como parámetro una
#lista de alumnos. La función debe buscar cuál es el alumno con el nombre más
#largo dentro de la lista y retornarlo.

def nombre_mas_largo(data_alumnos):
	may = 0
	for h in data_alumnos:
		if len(h[1]) > may:
			may = len(h[1])
			print("el nombre mas largo es: ",h[1])
	return may
	

#e) Realice un función llamada controlar_clave que recibe como parámetro un
#alumno,(legajo, nombre, apellido, contraseña). La función debe controlar si la
#contraseña es mayor a 6 caracteres y termina con un número, deberá imprimir un
#mensaje especificando el error cometido en caso de no cumplir las condiciones o
#bien imprimir los datos del alumno si la clave cumple con todas las condiciones.

def controlar_clave(data_alumnos):
	num = ("0","1","2","3","4","5","6","7","8","9")
	for k in data_alumnos:
		if (len(k[3]) > 6) and (k[3][-1] in num):
			print("los datos estan correctos")
			print(k)
  

#Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir
#del menú, el resto de las opciones permiten :
#- imprimir los datos de todos los alumnos con el formato pedido en el punto a)
#- imprimir los datos del alumno que tiene el legajo más chico.
#- imprimir los datos del alumno que tiene el nombre más largo.
#- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6
#caracteres y terminan con un número.



menu = "n1/ datos -- n2/ legajo mas chico -- n3/ nombre mas largo -- n4/ contraseña bien"
print(menu)
op = int(input("ingrese una opcion o 5 para salir: "))
while op != 5:
	if op == 1:
		data_alumnos = alumnos()
		print(data_alumnos)
	elif op == 2:
		print(legajo_menor(data_alumnos))
	elif op == 3:
		print(nombre_mas_largo(data_alumnos))
	elif op == 4:
		controlar_clave(data_alumnos)
	else:
		print("opcion incorrecta")
		print(menu)
	op = int(input("ingrese una opcion o 5 para salir: "))
		