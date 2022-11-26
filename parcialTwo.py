def cargaDeDatos () :
    lista = []
    legajo = int(input("Ingrese su legajo o 0 para finalizar: "))
    while legajo !=0:
        nombre= input("Introduzca su nombre: ")
        apellido= input("Introduzca su apellido: ")
        dni= input("Introduzca su DNI: ")
        email= input("Introduzca su mail: ")
        canMat= input("Introduzca las cantidad de materias aprobadas: ")
        data=(legajo, nombre, apellido, dni, email, canMat)
        lista.append(data)
        legajo = int(input("Ingrese su legajo o 0 para finalizar: "))
    print(lista)
    return lista



def funcionB (listaOriginal):
    listaNueva = []
    for x in listaOriginal:
        if x[1] !="" and x[2]!="" and x[3] !="" and x[4] !="" and x[5] !="":
            listaNueva.append(x)
        else:
            print("El alumno tiene algun dato incompleto", x)
    print(listaNueva)
    return listaNueva




def funcionC(listaOriginal, listaNueva):
    print("Lista original: ", listaOriginal)
    print("Cantidad de elementos de la lista original", len(listaOriginal))
    print("Lista nueva: ", listaNueva)
    print("Cantidad de elementos de la lista nueva", len(listaNueva))




def menu(listaOriginal):
    option=0
    while option != 3:
        print("Ingrese 1 para opcion B: ")
        print("Ingrese 2 para opcion C: ")
        print("Ingrese 3 para salir: ")
        option=int(input("Eliga una opcion: "))
        if option==1:
            listaNueva=funcionB(listaOriginal)
        elif option==2:
            funcionC(listaOriginal, listaNueva)

listaOriginal= cargaDeDatos()
menu(listaOriginal)
cargaDeDatos()



# # Nos contratan para realizar un sistema para un kiosco. De cada artículo se conoce
# # código, nombre, una descripción, el precio de venta, el nombre del proveedor y si es
# # necesaria la refrigeración del artículo (pudiendo ser R=requiere frío o N=no requiere frío).

# # a) Realice una función que cree una lista con información de artículos de kiosco. La
# # carga de artículos finaliza cuando se ingresa un artículo cuyo código = “999” y que
# # a la vez no requiera frío.

# # b) Realice una función que cree una lista con los datos del stock, donde de cada
# # articulo se conoce el código y la cantidad existente.

# # c) Se requiere imprimir los datos de todos los artículos que necesitan refrigeración o
# # los artículos que no la necesitan, dependiendo del valor ingresado por el usuario
# # (R=requiere frío o N=no requiere frío).

# # d) Se necesita imprimir la cantidad de artículos que necesitan refrigeración y la
# # cantidad de artículos que no la necesitan.

# # e) Se requiere imprimir los datos de los artículos cuyo stock es 0, de la siguiente
# # manera: Código, nombre del artículo, y nombre del proveedor.

# # f) Realice una función que utilizando la lista de productos creada en a) y en b)
# # genere una nueva lista con la información completa de los artículos que no
# # requieren frío, indicando además la cantidad existente.

# # Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir
# # del menú, el resto de las opciones permiten:
# # - imprimir los datos de los artículos que necesitan o no refrigeración, dependiendo
# # del valor ingresado por el usuario
# # - imprimir la cantidad de artículos que precisan refrigeración
# # - imprimir la cantidad de artículos que no requieren refrigeración
# # - imprimir los datos de los artículos cuyo stock es 0
# # - imprimir la información completa de los artículos que no requieren frío.


# # codigo, nombre, descripción, precioVenta, proveedor,

# def cargaDeArticulos ():
#     lista_Articulos = []
#     codigoArticulos = int(input("Ingrese el codigo del artículo: "))
#     refrigeracion = input("El articulo necesita refrigeración? s/n: ")
#     while codigoArticulos != 999 or refrigeracion != "n":
#         nombreArticulos = input("Ingrese el nombre del artículo: ")
#         descripcion = input("Ingrese el descripción del artículo: ")
#         precioVenta = int(input("Ingrese el precio de venta del artículo: "))
#         proveedor = input("Ingrese el proveedor del artículo: ")
#         datosDelArt = (codigoArticulos, refrigeracion, nombreArticulos, descripcion, precioVenta, proveedor)
#         lista_Articulos.append(datosDelArt)
#         codigoArticulos = int(input("Ingrese el codigo del artículo o 999 para finalizar: "))
#         refrigeracion = input("El articulo necesita refrigeración? s/n O n para finalizar: ")
#     print(lista_Articulos)
#     return lista_Articulos

# def datosStock (listaArticulos):
#     listaNueva = []
#     codigoArticulosTwo = int(input("Ingrese el codigo del stock: "))
#     cantidadDeArticulos = int(input("Ingrese la cantidad de articulos: "))
#     listaNueva.append(codigoArticulosTwo, cantidadDeArticulos)
#     return listaNueva


# def imprimirDatos(listaArticulos): 
#     listaSiR = []
#     listaNoR = []
#     for x in listaArticulos:
#         if x[0] != "999" and x[1] != "n":
#             listaSiR.append(x)
#         elif x[0] != 999 and x[1] == "n":
#             listaNoR.append(x)
#         print(f'Esta lista requiere refrigeracion: {listaSiR}')
#         print(f'Esta lista NO requiere refrigeracion: {listaNoR}')
#         print(f'La cantidad de articulos que necesitan refrigeracion es de {len(listaSiR)}')
#         print(f'La cantidad de articulos que NO necesitan refrigeracion es de {len(listaNoR)}')
#         return listaSiR, listaNoR

# # e) Se requiere imprimir los datos de los artículos cuyo stock es 0, de la siguiente
# # manera: Código, nombre del artículo, y nombre del proveedor.
# # def imprimirDatos (listaArticulos, datosStock):
# #     listaArticulosCero = []
# #     for x in listaArticulos:
# #         if x[0] != "999" and x[2] != "" and x[5] != "":
# #             listaArticulosCero.append(x)
        
# listaArticulos = cargaDeArticulos()
# cargaDeArticulos()

