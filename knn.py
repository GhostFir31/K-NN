
import LectorData
import MetodosDistancia

def calcularDistancias(MetodoDistancia,x,y):
    
    if(MetodoDistancia=="1"):
        return MetodosDistancia.distanciaEuclidiana(x,y)
    elif(MetodoDistancia=="2"):
        return MetodosDistancia.distanciaManhattan(x, y)
    elif(MetodoDistancia=="3"):
        
        p=input("escoga el valor de p: (p=1 es igual a Manhantan y p=2 es igual a Euclidiana)\n")
        
        return MetodosDistancia.distanciaMinkowski(x,y,int(p))
    
    else:
        print("Metodo no valido")
        

def knn(listaDatosBusqueda,listaDatosEntrenamiento,metodoDistancias):
    distancia=calcularDistancias(metodoDistancias,x,y)
    print("La distancia entre los puntos es: "+ str(distancia))
    pass

x = [10,28,35,42]
y = [51,64,75,86]

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
    
print("Escoja El Metodo de Calculo de Distancias: \n1)Euclidiana\n2)Manhattan\n3)Minkowski")    
nombreMetodo=input("Introduzca el numero del metodo a utilizar: \n")
print("x= "+str(x)+" y= "+str(y))    

knn(datosBusqueda,datosEntrenamiento,nombreMetodo)

