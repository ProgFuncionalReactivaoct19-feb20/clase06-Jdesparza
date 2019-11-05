"""
   	Jdesparza
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""
# para importar archivos csv
import csv

# para crear cada linea del archivo en diccionario
def lienasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

# para abrir el archivo
with open("data/data-estudiantes.csv") as midata:
	# para imprimir solo el apellido y una parte del email
	print(list(map(lambda x: "%s - %s"%(list(x.items())[0][1].split(" ")[1], \
		list(x.items())[1][1].split(".")[0]), lienasDiccionario(midata))))