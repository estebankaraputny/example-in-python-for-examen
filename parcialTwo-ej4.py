
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

def cursos():
	lista = []
	nombre = input("ingresar nombre del curso: ")
	while nombre != "fin":
		cant = int(input("ingrese la cantidad de clases: "))
		dia = input("ingrese dia de dictado: ")
		hora = int(input("ingrese hora de comienzo: "))
		dura = int(input("ingrese duracion en minutos: "))
		data = [nombre,cant,dia,hora,dura]
		if dura < 360:
			lista.append(data)
		nombre = input("ingresar nombre del curso: ")
	return lista

#a) Imprimir todos los cursos que tengan más de 5 clases

def curso_cantidad(curso_data):
	for x in curso_data:
		if x[1] >= 5:
			print(x)
	
#b) Imprimir los cursos que se dictan en un día de la semana indicado por el usuario.
def clase_dia(curso_data):
	didi = input("ingrese el dia que desea y se mostraran las clases: ")
	for j in curso_data:
		if didi == j[2]:
			print("ese dia estan los cursos: ",j)

#c) Imprimir el curso más intensivo (definido por la cantidad de clases y la duración de
#cada clase)

def intenso(curso_data):
	ca = 0
	dur = 0
	for h in curso_data:
		if h[1] > ca:
			ca = h[1]
	print("el curso con mas cantidad de clases es: ",h)
		if h[4] > dur:
			dur = h[4]
	print("el curso con mas duracion de clases es: ",h)

#d) Imprimir los datos en que se dicta un curso indicado por el usuario.
def curso_usu(curso_data):
	dat = input("ingrese materia y se mostraran sus datos: ")
	for l in curso_data:
		if dat == l[0]:
			print(l)

#e) Imprima todos los cursos que comienzan con una letra indicada por el usuario.
def letra(curso_data):
	le = input("ingrese letra y se mostrara los cursos correspondientes: ")
	for k in curso_data:
		if le == k[0][0]:
			print("el curso con la inicial es: ",k)


#El programa escrito deberá mostrar un menú para que el usuario elija la opción deseada.
#Importante: el sistema termina cuando el usuario elige la opción “salir”.
def menu():
	op = int(input("ingrese opcion: "))
	while op != 7:
		if op == 1:
			print(curso_data)
		elif op == 2:
			curso_cantidad(curso_data)
		elif op == 3:
			clase_dia(curso_data)
		elif op == 4:
			intenso(curso_data)
		elif op == 5:
			curso_usu(curso_data)
		elif op == 6:
			letra(curso_data)
		else:
			print("incorrecto")
		op = int(input("ingrese opcion: "))

curso_data = cursos() 
menuu = "n1/sus datos ingresados. n2/filtro de cursos menores. n3/ curso por dia. n4/ curso intenso. n5/ curso por nombre. n6/ curso por letra. n7/ salir"
print(menuu)
menu()