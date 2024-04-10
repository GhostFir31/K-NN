
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

def ordernarDistancias(listaDatosEntrenamiento, metodoDistancias, datoBusqueda):
    for linea in listaDatosEntrenamiento:
        distanciasPuntos = [float(val) for val in linea[:-1]] 
        distancia = calcularDistancias(metodoDistancias, datoBusqueda, distanciasPuntos)
        linea.append(distancia)  
        
    return listaDatosEntrenamiento

def knn(listaDatosBusqueda, listaDatosEntrenamiento, metodoDistancias, k, datoABuscar):
    datoBusqueda = [float(val) for val in listaDatosBusqueda[datoABuscar]]  
    print(datoBusqueda)
    
    listaconDistancias = ordernarDistancias(listaDatosEntrenamiento, metodoDistancias, datoBusqueda)
   
    listaconDistancias.sort(key=lambda x: x[-1])  
        
    k = int(k)
    listavaloresCercanos = listaconDistancias[:k]  
    
    print("K valores Cercanos :"+str(k))
    for fila in listavaloresCercanos:
        print(fila)
        
    
#nombreDatosBusqueda=input("Introduce el nombre del archivo de busqueda: \n")
#nombreDatosEntrenamiento=input("Introduce el nombre del archivo de entrenamiento: \n")

#datosBusqueda=LectorData.leerDatosBusqueda(nombreDatosBusqueda);
#datosEntrenamiento=LectorData.leerDatosEntrenamientoP(nombreDatosEntrenamiento);

datosBusqueda=LectorData.leerDatosBusquedaP();
datosEntrenamiento=LectorData.leerDatosEntrenamientoP();

categoriasEntrenamiento = LectorData.cantidadCategoria(datosEntrenamiento)
categoriasBusqueda = LectorData.cantidadCategoria(datosBusqueda)

print("Cantidad por categoria en datos para Entrenamiento:")
print("Datos para entrenamiento: ", len(datosEntrenamiento))
for categoria, cantidad in categoriasEntrenamiento.items():
    print("Categoria:", categoria, "Cantidad:", cantidad)

print("Cantidad por categoria en datos para Prueba:")
print("Datos para Prueba: ", len(datosBusqueda))
for categoria, cantidad in categoriasBusqueda.items():
    print("Categoria:", categoria, "Cantidad:", cantidad)
    
print("Escoja El Metodo de Calculo de Distancias: \n1)Euclidiana\n2)Manhattan\n3)Minkowski")    
nombreMetodo=input("Introduzca el numero del metodo a utilizar: \n")

k=input("Introduce el valor de vecinos cercanos k: \n")

knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,0)

