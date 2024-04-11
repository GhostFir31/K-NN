
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
    listaDatosEntrenamientoConDistancias = [linea[:] for linea in listaDatosEntrenamiento]
    
    for linea in listaDatosEntrenamientoConDistancias:
        distanciasPuntos = [float(val) for val in linea[:-1]] 
        distancia = calcularDistancias(metodoDistancias, datoBusqueda, distanciasPuntos)
        linea.append(distancia)  
        
    return listaDatosEntrenamientoConDistancias

def knn(listaDatosBusqueda, listaDatosEntrenamiento, metodoDistancias, k, datoABuscar):
    datoBusqueda = [float(val) for val in listaDatosBusqueda[datoABuscar]]  
    print("Punto de Busqueda: ")
    print(datoBusqueda)
    
    listaconDistancias = ordernarDistancias(listaDatosEntrenamiento, metodoDistancias, datoBusqueda)
    listaconDistancias.sort(key=lambda x: x[-1])      
    k = int(k)
    listavaloresCercanos = listaconDistancias[:k]  
    
    print("K valores Cercanos : k="+str(k))
    for fila in listavaloresCercanos:
        print(fila)
    prediccion(datoBusqueda,listavaloresCercanos)
        
def prediccion(datoBusqueda,listavaloresCercanos):
    
    clases = [fila[-2] for fila in listavaloresCercanos]
    
    cantidadClases = {}
    
    for clase in clases:
        if clase in cantidadClases:
            cantidadClases[clase] += 1
        else:
            cantidadClases[clase] = 1
    
    claseRepetidaMas = max(cantidadClases, key=cantidadClases.get)
            
    print("Prediccion: Clase "+str(claseRepetidaMas))        
    print("Realidad: Clase "+ str(int(datoBusqueda[-1])))

def ejecucionKNN(datosBusqueda,datosEntrenamiento,indice):
    print("Escoja El Metodo de Calculo de Distancias: \n1)Euclidiana\n2)Manhattan\n3)Minkowski")    
    nombreMetodo=input("Introduzca el numero del metodo a utilizar: \n")
    k=input("Introduce el valor de vecinos cercanos k: \n")

    knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,indice)

indice=0
    
nombreDatosBusqueda=input("Introduce el nombre del archivo de busqueda: \n")
nombreDatosEntrenamiento=input("Introduce el nombre del archivo de entrenamiento: \n")

datosBusqueda=LectorData.leerDatosBusqueda(nombreDatosBusqueda);
datosEntrenamiento=LectorData.leerDatosEntrenamiento(nombreDatosEntrenamiento);

#datosBusqueda=LectorData.leerDatosBusquedaP();
#datosEntrenamiento=LectorData.leerDatosEntrenamientoP();

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
    
ejecucionKNN(datosBusqueda,datosEntrenamiento,0)

opcion="a"

while(opcion!="s"):
    print("Escoga una opcion: \nc)Procesar El Siguiente Dato\nt)Procesar todos los datos de prueba\ns)Finalizar procesamiento")     
    opcion=input("")
    if opcion == "c":
        indice=indice+1
        ejecucionKNN(datosBusqueda,datosEntrenamiento,indice)
    elif opcion == "t":
        ejecucionKNN(datosBusqueda, datosEntrenamiento,0)
    elif opcion == "s":
        pass
    else:
        print("Opcion Introducida No Valida")

