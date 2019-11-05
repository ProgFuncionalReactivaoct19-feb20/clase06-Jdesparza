"""
   	Jdesparza
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""
# para importar archivos csv
import csv

# def lienas(archivo):
	# return csv.reader(archivo, delimiter=";")

# para crear cada linea del archivo en diccionario
def lienasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")
	
# para abrir el archivo
with open("data/data-estudiantes.csv") as midata:
	# print(list(lienasDiccionario(midata)))
	# para imprimir solo los nombres
	print(list(map(lambda x: list(x.items())[0][1], lienasDiccionario(midata))))