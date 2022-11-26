
#Ejercicio 5:
#Nos contratan para realizar un sistema para un kiosco. De cada artículo se conoce
#código, nombre, una descripción, el precio de venta, el nombre del proveedor y si es
#necesaria la refrigeración del artículo (pudiendo ser R=requiere frío o N=no requiere frío).
#a) Realice una función que cree una lista con información de artículos de kiosco. La
#carga de artículos finaliza cuando se ingresa un artículo cuyo código = “999” y que
#a la vez no requiera frío.

def kiosco():
	lista1 = []
	codigo = input("ingrese codigo: ")
	refri = input("ingrese R si requiere frio o N si no requiere: ")
	while codigo != "999" and refri != "n":
		nombre = input("ingrese nombre del producto: ") 
		desc = input("ingrese descripcion: ")
		precio = int(input("ingrese el precio: "))
		prov = input("ingrese el nombre del proveedor: ")
		data = [codigo,refri,nombre,desc,precio,prov]
		lista1.append(data)
		codigo = int(input("ingrese codigo: "))
		refri = input("ingrese R si requiere frio o N si no requiere: ")
	return lista1


#b) Realice una función que cree una lista con los datos del stock, donde de cada
#articulo se conoce el código y la cantidad existente.

def stock(kiosco_data):
	lista2 = []
	for x in kiosco_data:
		print("ingrese cantidad de stock de: ",x[2])
		cant = int(input("cantidad: "))
		data_stock = [x[2], x[0],cant]
		lista2.append(data_stock)
	return lista2
	

#c) Se requiere imprimir los datos de todos los artículos que necesitan refrigeración o
#los artículos que no la necesitan, dependiendo del valor ingresado por el usuario
#(R=requiere frío o N=no requiere frío).

def refri(kiosco_data):
	for k in kiosco_data:
		if k[1] == "r":
			print("requiere frio: ",k)
		elif k[1] == "n":
			print("no requiere frio",k)


kiosco_data = kiosco()
print(kiosco_data)
print(stock(kiosco_data))
refri(kiosco_data)

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

def datas():
	lista1 = []
	codigo = int(input("ingrese codigo: "))
	while codigo != -1:
		nombre = input("ingrese nombre del producto: ")
		cant = int(input("ingrese cantidad de producto: "))
		precio = int(input("ingrese el precio: "))
		datita = [codigo,nombre,cant,precio]
		lista1.append(datita)
		codigo = int(input("ingrese codigo: "))
	return lista1

def porcentaje(lista_data):
	cont = 0
	for x in lista_data:
		if x[2] < 10:
			cont = cont + 1
	tot = (cont * 100)
	print("el porcentaje es: ",tot /len(lista_data))

def menor(lista_data):
	cont = 999999
	for j in lista_data:
		if j[3] < cont:
			cont = j[3]
			nom = j[1]
	return cont,nom
	
def menu(lista_data):
	menuu = "op1/ datos ingresados. op2/ porcentajes. op3/ menor precio. op4/ salir"
	print(menuu)
	op = int(input("ingrese opcion: "))
	while op != 4:
		if op == 1:
			print(lista_data)
		if op == 2:
			print(porcentaje(lista_data))
		if op == 3:
			print(menor(lista_data))
	else:
		print(menuu)
	op = int(input("ingrese opcion: "))
	
		
lista_data = datas()
menu(lista_data)
