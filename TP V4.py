import os
import pickle
import os.path
from datetime import datetime
from datetime import date

#	1- ADMINISTRACIONES - (FALTA SILOS)
# 			B - PRODUCTOS - COMPLETO
#			C- RUBROS (COMPLETADO)
#			D- RUBROS POR PRODUCTO (COMPLETADO)
#			E- SILOS (FALTA CONFIRMAR)
#			A - F - G (EN CONSTRUCCION)

#	2- ENTREGA DE CUPOS - LISTO
#	3- RECEPCION - TODO LISTO menos FALTA VALIDAR FECHA CON PATENTE
#	4- REGISTRAR CALIDAD - FALTA TODO
#	5- REGISTRAR PESO BRUTO - FALTA TODO
#	6- REGISTRAR DESCARGA - FALTA TODO
#	7- REGISTRAR TARA - FALTA TODO
#	8- REPORTES - FALTA TODO
#	9- LISTADO DE SILOS RE CHAZOS - FALTA TODO

#	PARA TENER EN CUENTA: UNA FUNCION QUE VALIDE PATENTES (QUE LA PATENTE NO EXISTA Y QUE TENGA ENTRE 6 O 7 CARACTERES)
#
#


### Declaración De Arch ###


class TurnosCamiones:
    def __init__(self):
        self.patente = "" 
        self.cod_producto = 0
        self.tara = 0
        self.peso_bruto = 0
        self.estado = ""
        self.fecha_cupo = " " #AAAA/MM/DD
        self.fecha_rechazo = " "   

       # x = datetime.datetime.now() >> guarda la fecha de hoy con el formato: ano, mes, dia, hora ,minuto, segundo y microsegundo
       # x.year: ano
       # x.month: mes
       # print (x) imprime la fecha con todo lo de arriba
       # print (x.year) imprime solo el ano
       # print (x.month) imprime solo el mes
       # ...

       # para declarar una fecha podes utilizar x = datetime.datetime(2020, 5, 17) >> (17/5/2020)
       # https://www.w3schools.com/python/python_datetime.asp >> la info de la libreria .datetime

class Productos:
	def __init__(self):
		self.cod_producto = 0
		self.nom_producto = " "
		self.baja_logica = "X"

class Rubros:
    def __init__(self):
        self.cod_rubro = 0
        self.nom_rubro = " "

class RubrosXProducto:
    def __init__(self):
        self.cod_rubro = 0
        self.cod_producto = 0
        self.val_min = 0.00
        self.val_max = 100.00

class Silos:
    def __init__ (self):
        self.cod_silo = 0
        self.nom_productoSilo = " "
        self.cod_producto = 0
        self.stock = 0

### Formateo de datos antes de ingresos ###  
#def formatearTurnosCamiones(vrTurnosCamiones):

def formatearProductos(vrProd):
    vrProd.cod_producto = str(vrProd.cod_producto)
    vrProd.cod_producto = vrProd.cod_producto.ljust(20, " ") #codigo
    vrProd.nom_producto = vrProd.nom_producto.ljust(20, " ") #producto

def formatearRubros(vrRubro):
    vrRubro.cod_rubro = str(vrRubro.cod_rubro)
    vrRubro.cod_rubro = vrRubro.cod_rubro.ljust(20, " ") #codigo
    vrRubro.nom_rubro = vrRubro.nom_rubro.ljust(20, " ") #producto

def formatearRubrosXProducto(vrRubrosXProducto):
	vrRubrosXProducto.cod_rubro = str(vrRubrosXProducto.cod_rubro)
	vrRubrosXProducto.cod_rubro = vrRubrosXProducto.cod_rubro.ljust(20, " ")#codigo
	vrRubrosXProducto.cod_producto = str(vrRubrosXProducto.cod_producto)
	vrRubrosXProducto.cod_producto = vrRubrosXProducto.cod_producto.ljust(20, " ")#codigo
	vrRubrosXProducto.val_min = str(vrRubrosXProducto.val_min)
	vrRubrosXProducto.val_min = vrRubrosXProducto.val_min.ljust(20, " ")#valor minimo
	vrRubrosXProducto.val_max = str(vrRubrosXProducto.val_max)
	vrRubrosXProducto.val_max = vrRubrosXProducto.val_max.ljust(20, " ")#valor maximo

def formatearSilos(vrSilos):
	vrSilos.cod_silo = str(vrProd.cod_rubro)
	vrSilos.cod_silo = vrProd.cod_silo.ljust(20, " ") #codigo
	vrSilos.nom_productoSilo = vrProd.nom_productoSilo.ljust(20, " ") #producto
	vrSilos.stock = str(vrProd.stock)
	vrSilos.stock = vrProd.stock.ljust(20, " ") #stock

### Validaciones ###     
def validaRangoEnt(nro, desde, hasta):
	try:
		int(nro)
		if int(nro) >= desde and int(nro) <= hasta:
			return False
		else:
			return True
	except:
		return True

def validaRangoFloat(nro, desde, hasta):
	try:
		float(nro)
		if float(nro) >= desde and float(nro) <= hasta:
			return False
		else:
			return True
	except:
		return True


def hayProducto():
	t = os.path.getsize(afProductos)
	alProductos.seek(0)
	while alProductos.tell() <=t:
		pos = alProductos.tell()
		vrTemp = pickle.load(alProductos)
		if vrTemp.baja_logica == "A":
			return 1
	return -1
					

def buscaProducto(nom):
	global afProductos, alProductos
	nom = nom.ljust(20, " ")
	t = os.path.getsize(afProductos)
	alProductos.seek(0)
	while alProductos.tell() < t:
		pos = alProductos.tell()
		vrTemp = pickle.load(alProductos)
		if vrTemp.nom_producto == nom:
			return pos
	return -1
 
 
def buscaCodigo(cod):
	global afProductos, alProductos
	cod = str(cod)
	cod = cod.ljust(20, " ")
	t = os.path.getsize(afProductos)
	alProductos.seek(0)
	while alProductos.tell() < t:
		pos = alProductos.tell()
		vrTemp = pickle.load(alProductos)
		if vrTemp.cod_producto == cod:
			return True
	return False


def buscaSilo(silo):
	global afSilos, alSilos
	silo = silo.ljust(20, " ")
	t = os.path.getsize(afSiloss)
	alSilos.seek(0)
	while alSilos.tell()<t:
		pos = alSilos.tell()
		vrTemp = pickle.load(alSilos)
		if vrTemp.nom_productoSilo == silo:
			return pos 
	return -1


def buscaRubro(rub):
	global afRubros, alRubros
	rub = rub.ljust(20, " ")
	t = os.path.getsize(afRubros)
	alRubros.seek(0)
	while alRubros.tell()<t:
		pos = alRubros.tell()
		vrTemp = pickle.load(alRubros)
		if vrTemp.nom_rubro == rub:
			return pos 
	return -1


def buscaCodigoRubro(cod):
	global afRubros, alRubros
	cod = str(cod)
	cod = cod.ljust(20, " ")
	t = os.path.getsize(afRubros)
	alRubros.seek(0)
	while alRubros.tell() < t:
		pos = alRubros.tell()
		vrTemp = pickle.load(alRubros)
		if vrTemp.cod_rubro == cod:
			return True
	return False
	

def buscaSilo(nom):
	global afSilos, alSilos
	nom = nom.ljust(20, " ")
	t = os.path.getsize(afSilos)
	alSilos.seek(0)
	while alSilos.tell() < t:
		pos = alSilos.tell()
		vrTemp = pickle.load(alSilos)
		if vrTemp.nom_productoSilo == nom:
			return pos 
	return -1


def menuProd():
	global afProductos, alProductos
	opc = "X"
	prod = Productos()
	while opc != "v":
		os.system("cls")
		print('MENU PRODUCTOS')
		print("A - Alta")
		print("B - Baja")
		print("C - Consulta")
		print("M - Modificación")
		print("V - Volver al menu principal")
		opc = input("Ingrese la opción:")	
		opc = opc.lower()		
		if opc == "a":
			os.system("cls")
			print("Opción A - Alta de un Producto")
			print("-------------------------------")   
			print("Ingrese un producto para dar de alta")
			nom = input()
			nom = nom.lower()
			pos = buscaProducto(nom)
			if pos == -1:
				prod.nom_producto = nom
				prod.baja_logica = "A"
				print("Ingrese el código del producto")
				cod = input()
				while validaRangoEnt(cod, 0, 99999):
					cod = input("Ingrese un código valido")
				while buscaCodigo(cod):
					cod = input("Código ya utilizado. Ingrese otro:")
				prod.cod_producto = cod 
				formatearProductos(prod) 
				pickle.dump(prod, alProductos)
				alProductos.flush()
				print("Alta de producto realizada")
			else:
				alProductos.seek(pos, 0)
				prod = pickle.load(alProductos)
				if prod.baja_logica == "B":
					print("Ingrese el código del producto")
					cod = input()
					while validaRangoEnt(cod, 0, 99999):
						cod = input("Ingrese un código valido")
					while buscaCodigo(cod):
						cod = input("Código ya utilizado. Ingrese otro:")
					alProductos.seek(pos)
					prod.nom_producto = nom
					prod.baja_logica = "A"
					prod.cod_producto = cod 
					formatearProductos(prod) 
					pickle.dump(prod, alProductos)
					alProductos.flush()
					print("Alta de producto realizada")
					os.system("pause")
				else: 
					print("Producto ya registrado")
					os.system("pause") 

		if opc == "b":
			prod = Productos()
			os.system("cls")
			print("Ingrese el producto a dar de baja")
			nom  = input()
			nom = nom.lower()
			pos = buscaProducto(nom)
			if pos == -1:
				print("Producto no encontrado")
				os.system("pause")
			else:
				alProductos.seek(pos, 0)
				productos = pickle.load(alProductos)
				if productos.baja_logica == "A":
					alProductos.seek(pos, 0)
					prod.nom_producto = nom
					prod.baja_logica = "B"
					formatearProductos(prod) 
					pickle.dump(prod, alProductos)
					alProductos.flush()
					print("Baja de producto realizada")
					os.system("pause")
				else: 
					print("Producto ya dado de baja")
					os.system("pause") 
		

		if opc == "m":
			prod = Productos()
			os.system("cls")
			print("Opción M - Modificación de un producto")
			print("---------------------------------------")
			print("Ingrese un producto para modificar")
			nom = input()
			nom = nom.lower()
			pos = buscaProducto(nom)
			if pos == -1:
				print("Producto no registrado")
				os.system("pause")
			else:
				print("Ingrese el nuevo producto")
				mod = input()
				pos2 = buscaProducto(mod)
				if pos2 == -1:
					print("Ingrese el código del producto")
					cod = input()
					while validaRangoEnt(cod, 0, 99999):
						cod = input("Ingrese un código valido")
					while buscaCodigo(cod):
						cod = input("Código ya utilizado. Ingrese otro:")
					alProductos.seek(pos)
					prod.nom_producto = mod
					prod.baja_logica = "A"
					prod.cod_producto = cod 
					formatearProductos(prod) 
					pickle.dump(prod, alProductos)
					alProductos.flush()
					print("Modificación realizada")
					os.system("pause")
				else:
					print("Producto ya registrado")
					os.system("pause")



		if opc == "c":
			os.system("cls")
			print("Opción C - Consulta")
			print("---------------------")
			t = os.path.getsize(afProductos)
			alProductos.seek(0)
			while alProductos.tell() < t:
				prod = pickle.load(alProductos)
				print("Producto:", prod.nom_producto)
				print("Código:", prod.cod_producto)
				print("Estado:", prod.baja_logica)
				os.system("pause")

			
 
def menuRubro():
	global afRubros, alRubros
	opc = "X"
	while opc != "v":
		os.system("cls")
		print('MENU RUBRO')
		print("A - Alta")
		print("B - Baja")
		print("C - Consulta")
		print("M - Modificación")
		print("V - Volver al menu principal")
		opc = input("Ingrese la opción:")
		opc = opc.lower()
		if opc == "a":
			os.system("cls")
			print("Opción A - Alta de un rubro")
			print("-------------------------------")
			print("Qué rubro quiere dar de alta?") 
			rub = input()
			rub = rub.lower()
			prod = Rubros()
			if buscaRubro(rub) == -1:
				prod.nom_rubro = rub
				print("Ingrese el código del rubro")
				cod = input()
				while validaRangoEnt(cod, 0, 99999):
					cod = input("Ingrese un código valido")
				while buscaCodigoRubro(cod):
					cod = input("Código ya utilizado. Ingrese otro:")
				prod.cod_rubro = cod 
				formatearRubros(prod)
				pickle.dump(prod, alRubros)
				alRubros.flush()
				input("Alta de rubro realizada")
			else:
				print("Rubro ya registrado")
			os.system("pause")
		else:
			input("Esta opcion esta en desarrollo")



def menuRubroXProducto(): 
	opc = "X"
	prod = Productos()
	rubro = Rubros()
	rxp = RubrosXProducto()
	while opc != "v":
		os.system("cls")
		print('MENU RUBRO POR PRODUCTOS')
		print("A - Alta")
		print("B - Baja")
		print("C - Consulta")
		print("M - Modificación")
		print("V - Volver al menu principal")
		opc = input("Ingrese la opción:")
		opc = opc.lower()
		if opc == "a":
			os.system('cls')
			print("Opción A - Alta de un Rubro x Producto")
			print("-------------------------------") 
			if not hayProducto() ==- 1: ## Verifica que hay productos para elegir
				if os.path.getsize(afRubros) > 0: ## Verifica que hay rubros para elegir
					print("Ingrese un producto para asignarle un rubro")
					nom = input()
					nom = nom.lower()
					pos = buscaProducto(nom)
					while pos == -1:
						t = os.path.getsize(afProductos)
						alProductos.seek(0)
						while alProductos.tell() < t:
							prod = pickle.load(alProductos)
							print("Producto:", prod.nom_producto)
							print("Código:", prod.cod_producto)
							print("Estado:", prod.baja_logica)
							os.system("pause")
						print("Ingrese un producto dado de alta previamente")
						nom = input()
						nom = nom.lower()
						pos = buscaProducto(nom)
					nom = nom.ljust(20, " ")
					os.system("cls") 
					alProductos.seek(pos, 0)
					prod = pickle.load(alProductos)
					codprod = prod.cod_producto
					print("Ingrese un rubro para asignarle al producto ingresado")
					rub = input()
					rub = rub.lower()
					while buscaRubro(rub) == -1: #Valida Rubro
						print(rubro)
						print("Ingrese un rubro dado de alta previamente")
						rub = input()
						rub = rub.lower()
					rub = rub.ljust(20, " ")
					os.system("cls") 
					pos = buscaRubro(rub)
					alRubros.seek(pos, 0)
					rubro = pickle.load(alRubros)
					rxp.cod_producto = codprod
					rxp.cod_rubro = rubro.cod_rubro
					min = input("Ingrese el valor del parametro minimo:")
					max = input("Ingrese el valor del parametro maximo:")
					while not(((validaRangoFloat(min, 0.00, 100.00) == False) and (validaRangoFloat(max, 0.00, 100.00) == False) and (min < max))): #Valida Min Max
						min = input("Reingrese el valor del parametro minimo:")
						max = input("Reingrese el valor del parametro maximo:")
						os.system("cls")
					rxp.val_min = min
					rxp.val_max = max
					formatearRubrosXProducto(rxp) #revisar funciton not defined en linea 87
					pickle.dump(rxp, alRubrosXProducto)
					alRubrosXProducto.flush()
					print("Carga exitosa")
					os.system("pause")
				else:
					input("No hay rubros dados de alta")
					os.system("pause")

			else:
				input("No hay productos dados de alta")
				os.system("pause")

		elif opc != "v":
			input("Esta opcion esta en desarrollo")
			os.system("pause") 
		
		


def menuSilos(): 
	
	opc = "X"
	while opc != "v":
		os.system("cls")
		print("A - Alta")
		print("B - Baja")
		print("C - Consulta")
		print("M - Modificación")
		print("V - Volver al menu principal")
		opc = input("Ingrese la opción:")
		opc = opc.lower()
		if opc == "a":
			os.system("cls")
			print("Opción A - Alta de un silo")
			print("-------------------------------")   
			print("Qué silo quiere dar de alta?")
			nom = input()
			nom = nom.lower()
			pos = buscaProducto(nom)
			if pos == -1:
				print("Debe registrar el producto para poder dar de alta el silo")
				os.system("pause")
			else:
				alProductos.seek(pos, 0)
				prod = pickle.load(alProductos)
				if prod.baja_logica == "B":
					print("El producto esta dado de baja")
					os.system("pause")
				else:
					if buscaSilo(nom) == -1:
						silo = Silos()
						alProductos.seek(pos, 0)
						prod = pickle.load(alProductos)
						silo.nom_productoSilo = nom
						silo.cod_silo = prod.cod_producto 
						pickle.dump(silo, alSilos)
						alSilos.flush()
						print("Alta de silo realizada")
						os.system("pause")
					else:
						print("Silo ya registrado")
						os.system("pause")
		else:
			print("Esta opcion esta en desarrollo")
			os.system("pause")


# BUSCAR FECHA
def buscafecha(fecha, pat):
	global afMenuCamiones, alMenuCamiones
	t = os.path.getsize(afMenuCamiones)
	alMenuCamiones.seek(0)
	while alMenuCamiones.tell() < t:
		pos = alMenuCamiones.tell()
		vrTemp = pickle.load(alMenuCamiones)
		if (vrTemp.fecha_cupo) == fecha and vrTemp.patente == pat:
			return pos 			
	return -1


def buscaPatente(pat):
	global afMenuCamiones, alMenuCamiones
	t = os.path.getsize(afMenuCamiones)
	vrTemp = TurnosCamiones()
	alMenuCamiones.seek(0)
	while alMenuCamiones.tell() < t:
		pos = alMenuCamiones.tell()
		vrTemp = pickle.load(alMenuCamiones)
		if vrTemp.patente == pat:
			return pos
	return -1


# ENTREGA DE CUPOS #
def Cupos():
	os.system("cls")
	print("Opción 2 - Cupos")
	print("------------------")
	nom = "X"
	while nom != "*":
		print("Para qué producto requiere el cupo? [* para salir]")
		nom = input()
		nom = nom.lower()
		pos = buscaProducto(nom)
		if nom != "*":
			if pos == -1:
				print("Producto no registrado")
			else:
				alProductos.seek(pos, 0)
				prod = pickle.load(alProductos)
				if prod.baja_logica == "B":
					print("Producto dado de baja")
				else:
					turnos = TurnosCamiones()
					fecha_hoy = date.today()                  #formato aaaa-mm-dd#
					fecha_hoy = str(fecha_hoy)                #convertimos a string#
					ah, mh, dh = fecha_hoy.split("-")         #separa en variables particulares, dh = dia hoy #
					fecha_hoy = dh + "/" + mh + "/" + ah      #formato dd/mm/aaaa#		
					print("Ingrese la patente:")
					pat = input()
					while len(pat) < 6 or len(pat) > 7 :
						print("Patente invalida. Ingrese una patente entre 6 y 7 caracteres")
						pat = input() 					
					flag = True
					while flag:
						try:
							fecha = input("Fecha de recepción en formato DD/MM/AAAA: ") 
							datetime.strptime(fecha, "%d/%m/%Y")  
							fecha = str(fecha)                              																	#valida la fecha#
							dc, mc, ac = fecha.split("/")                                               										 #separa en variables particulares, dc = dia cupo#
							if ac > ah or ac == ah and mc > mh or ac == ah and mc == mh and dc > dh or ac == ah and mc == mh and dc == dh:	   	 #verifica que fecha cupo sea mayor a hoy#
								if buscafecha(fecha, pat) == -1:
									alProductos.seek(pos)
									prod = pickle.load(alProductos)
									turnos.fecha_cupo = fecha
									turnos.cod_producto = prod.cod_producto
									turnos.estado = "P"
									turnos.patente = pat 
									pickle.dump(turnos, alMenuCamiones)
									alMenuCamiones.flush()
									os.system('cls')
									print("Cupo asignado correctamente")
									os.system('pause')
									os.system('cls')
									flag = False
								else:
									print("Cupo ya asignado")
									flag = False
							else:
								print("Fecha invalida")
								os.system("pause")
						except:
							print("Fecha invalida")
							os.system("pause")	

# RECEPCION #

def Recepcion():
	global afMenuCamiones, alMenuCamiones
	turnos = TurnosCamiones()
	os.system("cls")
	print("Opción 3 - Recepción")
	print("---------------------")
	fecha_hoy = date.today()
	fecha_hoy = str(fecha_hoy)
	ah, mh, dh = fecha_hoy.split("-")
	fecha_hoy = dh + "/"+ mh + "/" + ah
	pat = "a"
	while pat != "*":
		print("Ingrese la patente [* para salir]:")
		pat = input()
		if pat != "*":
			pos = buscaPatente(pat)
			if pos == -1:
				print("Patente no registrada")
				os.system("pause")
			else:
				if buscafecha(fecha_hoy, pat) == pos:
					pos = buscaPatente(pat)
					alMenuCamiones.seek(pos)
					turnos = pickle.load(alMenuCamiones)
					if turnos.estado == "P":
						turnos.estado = "A"
						pos = buscaPatente(pat)
						alMenuCamiones.seek(pos)
						pickle.dump(turnos, alMenuCamiones)
						alMenuCamiones.flush()
						print("Camión recibido")
						os.system("pause")
					else:
						print("Camión en otro estado")
						os.system("pause")
				else:
					print("El camión no tiene cupo para la fecha de hoy")
					os.system("pause")


def patArribada(pat):
	global afMenuCamiones, alMenuCamiones
	t = os.path.getsize(afMenuCamiones)
	alMenuCamiones.seek(0)
	while alMenuCamiones.tell() < t:
		pos = alMenuCamiones.tell()
		vrTemp = pickle.load(alMenuCamiones)
		if vrTemp.patente == pat and vrTemp.estado == "A":
			return pos 
	return -1


def patConCalidad(pat):
	global afMenuCamiones, alMenuCamiones
	t = os.path.getsize(afMenuCamiones)
	alMenuCamiones.seek(0)
	while alMenuCamiones.tell() < t:
		pos = alMenuCamiones.tell()
		vrTemp = pickle.load(alMenuCamiones)
		if vrTemp.patente == pat and vrTemp.estado == "C":
			return pos 
	return -1

def patConPesoBruto(pat):
	global afMenuCamiones, alMenuCamiones
	t = os.path.getsize(afMenuCamiones)
	alMenuCamiones.seek(0)
	while alMenuCamiones.tell() < t:
		pos = alMenuCamiones.tell()
		vrTemp = pickle.load(alMenuCamiones)
		if vrTemp.patente == pat and vrTemp.estado == "B":
			return pos 
	return -1


def Calidad():
	global afMenuCamiones, alMenuCamiones,  afRubrosXProducto, alRubrosXProducto
	os.system("cls")
	print("Opción 4 - Registrar calidad")
	print("-------------------------------")
	turnos = TurnosCamiones()
	fecha_hoy = date.today()
	fecha_hoy = str(fecha_hoy)
	ah, mh, dh = fecha_hoy.split("-")
	fecha_hoy = dh + "/"+ mh + "/" + ah
	print("Ingrese la patente:")
	pat = input()
	pos = buscaPatente(pat)
	bandera = 0
	if pos == -1:
		print("Patente no registrada")
		os.system("pause")
	else:
		pos = patArribada(pat)
		if pos == -1:
			print("Camión no arribado")
			os.system("pause")
		else:
			mal = 0 
			alMenuCamiones.seek(pos, 0)
			turnos = pickle.load(alMenuCamiones)
			cod = turnos.cod_producto
			print("Código del producto: ", turnos.cod_producto)
			t = os.path.getsize(afRubrosXProducto)
			alRubrosXProducto.seek(0)
			cod = cod.ljust(20, " ")
			while alRubrosXProducto.tell() < t:
				if mal == 3:
					break
				if bandera == 1:
					break
				bandera = 0
				pos = alRubrosXProducto.tell()
				vrTemp = pickle.load(alRubrosXProducto)
				if vrTemp.cod_producto == cod:
					alRubrosXProducto.seek(pos, 0)
					mi = vrTemp.val_min
					ma = vrTemp.val_max
					mi = mi.replace(" ","")
					ma = ma.replace(" ","")
					mi = int(mi)
					ma = int(ma)
					cod1 = vrTemp.cod_rubro
					t2 = os.path.getsize(afRubros)
					alRubros.seek(0)
					while alRubros.tell() < t2 and mal < 3:
						vrTemp2 = pickle.load(alRubros)
						pos2 = alRubros.tell()
						if vrTemp2.cod_rubro == cod1:
							print("Rubro: ", vrTemp2.nom_rubro)
							print("Valor minimo: ", vrTemp.val_min, "Valor maximo: ", vrTemp.val_max)
							valor = input("Valor del rubro: ")
							if validaRangoFloat(valor, mi, ma) == True:
								mal = mal + 1
							else:
								posicionPatente = buscaPatente(pat)
								alMenuCamiones.seek(posicionPatente)
								turnos = pickle.load(alMenuCamiones)
								turnos.estado = "C"
								posicionPatente = buscaPatente(pat)
								alMenuCamiones.seek(posicionPatente)
								pickle.dump(turnos, alMenuCamiones)
								alMenuCamiones.flush()
								print("Camión registrado con calidad")
								os.system("pause")
								bandera = 1
								break
					

			if mal == 3:	
				fecha_hoy = date.today()                  #formato aaaa-mm-dd#
				fecha_hoy = str(fecha_hoy)                #convertimos a string#
				ah, mh, dh = fecha_hoy.split("-")         #separa en variables particulares, dh = dia hoy #
				fecha_hoy = dh + "/" + mh + "/" + ah      #formato dd/mm/aaaa#		`


				posicionPatente = buscaPatente(pat)
				alMenuCamiones.seek(posicionPatente)
				turnos = pickle.load(alMenuCamiones)
				turnos.estado = "R"
				turnos.fecha_rechazo = fecha_hoy
				pickle.dump(turnos, alMenuCamiones)
				alMenuCamiones.flush()
				os.system("cls")
				print ("Camión rechazado por tener valores fuera de los limites asignados al rubro por producto.")
				os.system("pause")


def pBruto():
	global afMenuCamiones, alMenuCamiones
	os.system('cls')
	print ("REGISTRAR PESO BRUTO")
	
	print("Ingrese la patente o * para salir:")
	pat = input()
	bandera = 0
	if pat != "*":
		pos = buscaPatente(pat)
		if pos == -1:
			print("Patente no registrada")
			os.system("pause")
		else:
			pos = patConCalidad(pat)
			if pos == -1:
				print("El Camion no cumple con la Calidad.")
				os.system("pause")
			else: 
				pBruto = input("Ingrese peso bruto en kg: ")

				posicionPatente = buscaPatente(pat)
				alMenuCamiones.seek(posicionPatente)
				turnos = pickle.load(alMenuCamiones)
				turnos.estado = "B"
				turnos.peso_bruto = pBruto
				posicionPatente = buscaPatente(pat)
				alMenuCamiones.seek(posicionPatente)
				pickle.dump(turnos, alMenuCamiones)
				alMenuCamiones.flush()
				print("Peso Bruto registrado correctamente: ", turnos.peso_bruto,"kg")
				os.system("pause")



def Tara():
	global afMenuCamiones, alMenuCamiones
	os.system('cls')
	print ("=====REGISTRAR TARA=====")
	turnos = TurnosCamiones()
	print("Ingrese la patente o * para salir:")
	pat = input()
	bandera = 0
	tara = 0
	if pat != "*":
		pos = buscaPatente(pat)
		if pos == -1:
			print("Patente no registrada")
			os.system("pause")
		else:
			pos = patConPesoBruto(pat)
			if pos == -1:
				print("Se debe registrar el peso bruto del camion antes que la tara.")
				os.system("pause")
			else: 
				posicionPatente = buscaPatente(pat)
				alMenuCamiones.seek(posicionPatente)
				turnos = pickle.load(alMenuCamiones)
				bruto = turnos.peso_bruto
				bruto = float(bruto)
				tara = float(tara)
				while tara >= bruto or tara == 0:
					tara = input("Ingrese tara del camion en kg: ")
					tara = float(tara)
					if tara > bruto:
						print ("El peso de la tara no puede ser mayor al peso bruto del camion por favor reingrese: ")
					if tara == bruto:
						print ("El camion no puede estar vacio.")

				posicionPatente = buscaPatente(pat)
				alMenuCamiones.seek(posicionPatente)
				turnos = pickle.load(alMenuCamiones)
				turnos.estado = "F"
				turnos.tara = tara
				posicionPatente = buscaPatente(pat)
				alMenuCamiones.seek(posicionPatente)
				pickle.dump(turnos, alMenuCamiones)
				alMenuCamiones.flush()
				print("Tara registrada correctamente registrado correctamente: ", turnos.tara,"kg")
				os.system("pause")
				os.system('cls')
				print("Datos del camion:")
				print("Patente:", turnos.patente)
				print("Peso Bruto", turnos.peso_bruto, "kg")
				print("Tara: ", turnos.tara, "kg")
				print("Estado: ", turnos.estado)
				print("El camion fue entregado con exito! Cambiando estado a Finalizado...")
				os.system('pause')






def mostrarSubmenu():
	os.system("cls")
	print("A - Titulares")
	print("B - Productos")
	print("C - Rubros")
	print("D - Rubros por producto")
	print("E - Silos")
	print("F - Sucursales")
	print("G - Producto por titular")
	print("V - Volver al menu principal")

def Admin():
	mostrarSubmenu()
	opc = "X"
	while opc != "v":
		opc = input("Ingrese la opción:")
		opc = opc.lower()
		if opc == "a":
			print("Esta funcionalidad está en construcción")
			os.system("pause")
		elif opc == "b":
			menuProd()
		elif opc == "c":
			menuRubro()
		elif opc == "d":
			menuRubroXProducto()
		elif opc == "e":
			menuSilos()
		elif opc == "f":
			print("Esta funcionalidad está en construcción")
			os.system("pause")
		elif opc == "g":
			print("Esta funcionalidad está en construcción")
			os.system("pause")
		mostrarSubmenu()
		




os.makedirs("c:\\programas", exist_ok=True)  


afMenuCamiones = "c:\\programas\\camiones.dat"
if not os.path.exists(afMenuCamiones):
	alMenuCamiones = open(afMenuCamiones, "w+b")
else:
	alMenuCamiones = open(afMenuCamiones, "r+b")

afProductos = "c:\\programas\\productos.dat"
if not os.path.exists(afProductos):
	alProductos = open(afProductos, "w+b")
else:
	alProductos = open(afProductos, "r+b")

afRubros = "c:\\programas\\rubros.dat"
if not os.path.exists(afRubros):
	alRubros = open(afRubros, "w+b")
else:
	alRubros = open(afRubros, "r+b")

afRubrosXProducto = "c:\\programas\\rubrosxproducto.dat"
if not os.path.exists(afRubrosXProducto):
	alRubrosXProducto = open(afRubrosXProducto, "w+b")
else:
	alRubrosXProducto = open(afRubrosXProducto, "r+b")

afSilos = "c:\\programas\\silos.dat"
if not os.path.exists(afSilos):
	alSilos = open(afSilos, "w+b")
else:
	alSilos = open(afSilos, "r+b")


def mostrarMenu():
	os.system("cls")
	print("Menu de Opciones")
	print("----------------------")
	print("1 - Administraciones")
	print("2 - Entrega de cupos")
	print("3 - Recepción")
	print("4 - Registrar calidad")
	print("5 - Registrar peso bruto")
	print("6 - Registrar descarga")
	print("7 - Registrar tara")
	print("8 - Reportes")
	print("9 - Listado de silos y rechazos")
	print("0 - Salir")

opc = -1
while opc != 0:
	mostrarMenu()
	opc = input("Ingrese la opción:")
	while validaRangoEnt(opc, 0, 9):
		opc = input("Incorrecto - Ingrese opción [0-9]:")
	opc = int(opc)
	if opc == 1:
		Admin()
	elif opc == 2:
		Cupos()
	elif opc == 3:
		Recepcion()
	elif opc == 4:
		Calidad()
	elif opc == 5:
		pBruto()
	elif opc == 6:
		Descarga()
	elif opc == 7:
		Tara()
	elif opc == 8:
		Reportes()
	elif opc == 9:
		Silos()
	else:
		alMenuCamiones.close()
		alProductos.close()
		alRubros.close()
		alRubrosXProducto.close()
		alSilos.close()