"""
   	Jdesparza
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""
# para importar archivos csv
import csv
# para leer cada linea del archivo delimitadas por ;
def lineas(archivo):
	return csv.reader(archivo, delimiter=";")
# para abrir el archivo
with open("data/data-estudiantes.csv") as midata:
	"""
		lista = list(lineas(midata))
		lista1 = map(lambda x: x[1], lista)
		lista2 = list(filter( lambda x: x != "email", lista1))
		print(lista2)
	"""
	# para imprimir solo los emails
	print(list(filter(lambda x: x != "email", map(lambda x: x[1], lineas(midata)))))

# midata = open("data/data-estudiantes.csv") # en usos de archivos de grandes volumenes de \
	# datos es necesario cerrar el archivo
# print(list(lineas(midata)))
# midata.close()