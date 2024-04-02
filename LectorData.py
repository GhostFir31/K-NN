import csv
from random import shuffle

def leer_csv(archivo_csv):
    datos = []
    with open(archivo_csv, 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def dividir_datos(datos, porcentaje_entrenamiento):
    total_datos = len(datos)
    cantidad_entrenamiento = int(total_datos * porcentaje_entrenamiento / 100)
    
    datos_entrenamiento = datos[:cantidad_entrenamiento]
    datos_busqueda = datos[cantidad_entrenamiento:]
    
    return datos_entrenamiento, datos_busqueda

def contar_cantidad_por_categoria(lista):
    categorias = {}
    for fila in lista:
        categoria = fila[-1]  
        if categoria not in categorias:
            categorias[categoria] = 1
        else:
            categorias[categoria] += 1
    
    categorias_ordenadas = {}
    for categoria_num in range(5):  
        if str(categoria_num) in categorias:
            categorias_ordenadas[str(categoria_num)] = categorias[str(categoria_num)]
    
    return categorias_ordenadas

archivo_csv = "Datos_sujeto1 - Datos_sujeto1.csv"
datos = leer_csv(archivo_csv)

shuffle(datos)

porcentaje_entrenamiento = int(input("Porcentaje de datos para entrenamiento (0-100): "))
porcentaje_busqueda = 100 - porcentaje_entrenamiento

datos_entrenamiento, datos_busqueda = dividir_datos(datos, porcentaje_entrenamiento)

print("*-----------------------------------------Datos para entrenamiento-----------------------------------------*")
for fila in datos_entrenamiento:
    print(fila)

print("*-----------------------------------------Datos para búsqueda-----------------------------------------*")
for fila in datos_busqueda:
    print(fila)


categorias_entrenamiento = contar_cantidad_por_categoria(datos_entrenamiento)
categorias_busqueda = contar_cantidad_por_categoria(datos_busqueda)

print("Cantidad por categoría en datos para entrenamiento:")
print("Datos para entrenamiento: ", len(datos_entrenamiento))
for categoria, cantidad in categorias_entrenamiento.items():
    print("Categoría:", categoria, "Cantidad:", cantidad)

print("Cantidad por categoría en datos para búsqueda:")
print("Datos para búsqueda: ", len(datos_busqueda))
for categoria, cantidad in categorias_busqueda.items():
    print("Categoría:", categoria, "Cantidad:", cantidad)