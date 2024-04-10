import csv
from random import shuffle


def leerCsv(archivo_csv):
    datos = []
    with open(archivo_csv, 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def leerDatosBusqueda(nombre):
    archivo_csv = nombre+".csv"
    datos = leerCsv(archivo_csv)
    shuffle(datos)
    return datos

def leerDatosEntrenamiento(nombre):
    archivo_csv = nombre+".csv"
    datos = leerCsv(archivo_csv)
    shuffle(datos)
    return datos 

def leerDatosBusquedaP():
    archivo_csv = "datosBusqueda.csv"
    datos = leerCsv(archivo_csv)
    shuffle(datos)
    return datos

def leerDatosEntrenamientoP():
    archivo_csv = "datosEntrenamiento.csv"
    datos = leerCsv(archivo_csv)
    shuffle(datos)
    return datos 

def cantidadCategoria(datos):
    categorias = {}
    for fila in datos:
        categoria = fila[-1]
        if categoria not in categorias:
            categorias[categoria] = 1
        else:
            categorias[categoria] += 1
    
    categoriasOrdenadas = {}
    for categoriaNum in range(5):
        if str(categoriaNum) in categorias:
            categoriasOrdenadas[str(categoriaNum)] = categorias[str(categoriaNum)]
    
    return categoriasOrdenadas


"""""
datosBusqueda=leerDatosBusqueda();
datosEntrenamiento=leerDatosEntrenamiento();

print("*-----------------------------------------Datos para entrenamiento-----------------------------------------*")
for fila in datosEntrenamiento:
    print(fila)

print("*-----------------------------------------Datos para búsqueda-----------------------------------------*")
for fila in datosBusqueda:
    print(fila)

categoriasEntrenamiento = cantidadCategoria(datosEntrenamiento)
categoriasBusqueda = cantidadCategoria(datosBusqueda)

print("Cantidad por categoría en datos para Entrenamiento:")
print("Datos para entrenamiento: ", len(datosEntrenamiento))
for categoria, cantidad in categoriasEntrenamiento.items():
    print("Categoria:", categoria, "Cantidad:", cantidad)

print("Cantidad por categoría en datos para Prueba:")
print("Datos para Prueba: ", len(datosBusqueda))
for categoria, cantidad in categoriasBusqueda.items():
    print("Categoria:", categoria, "Cantidad:", cantidad)
    """""