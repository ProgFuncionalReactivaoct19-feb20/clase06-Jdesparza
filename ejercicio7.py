"""
   	Jdesparza
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""
import csv

# para crear cada linea del archivo en diccionario
def lienasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter="\t")

# para abrir el archivo
with open("data/trabajadores.csv") as midata:
	lista = list(lienasDiccionario(midata))
	# se imprime solo las listas con una longitud mayor a 10 en los paises
	print("%s\n\n%s\n\n"%("LISTAS CON UNA LONGITUD MAYOR A 10 EN LOS PAISES", \
		list(filter(lambda x: len(list(x.items())[2][1]) > 10, lista))))
	# se imprime las listas ordenadas segun el dia de nacimiento
	print("%s\n\n%s"%("LISTAS ORDENADAS SEGUN EL DIA DE NACIMIENTO", \
		sorted(lista, key = lambda x: list(x.items())[1][1].split("-")[2])))