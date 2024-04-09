import LectorData

datosBusqueda=LectorData.leerDatosBusqueda();
datosEntrenamiento=LectorData.leerDatosEntrenamiento();

categoriasEntrenamiento =LectorData. cantidadCategoria(datosEntrenamiento)
categoriasBusqueda = LectorData.cantidadCategoria(datosBusqueda)

print("Cantidad por categoría en datos para Entrenamiento:")
print("Datos para entrenamiento: ", len(datosEntrenamiento))
for categoria, cantidad in categoriasEntrenamiento.items():
    print("Categoria:", categoria, "Cantidad:", cantidad)

print("Cantidad por categoría en datos para Prueba:")
print("Datos para Prueba: ", len(datosBusqueda))
for categoria, cantidad in categoriasBusqueda.items():
    print("Categoria:", categoria, "Cantidad:", cantidad)
    
    
def estimarDistancia():
    
    pass
def knn():
    
    pass

