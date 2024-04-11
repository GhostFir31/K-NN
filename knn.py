
import LectorData
import MetodosDistancia

def calcularDistancias(MetodoDistancia,x,y):
    
    if(MetodoDistancia=="1"):
        return MetodosDistancia.distanciaEuclidiana(x,y)
    elif(MetodoDistancia=="2"):
        return MetodosDistancia.distanciaManhattan(x, y)
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

def ejecucionKNN(datosBusqueda,datosEntrenamiento):
    print("*-----------------------------------------Datos para búsqueda-----------------------------------------*")
    for fila in datosBusqueda:
        print("No." + str(numDato) + " " + ", ".join(map(str, fila)))
        numDato = numDato + 1
        
    datoABuscar=int(input("Escoga el numero de Dato que quiere Clasificar: \n"))
    print("Escoja El Metodo de Calculo de Distancias: \n1)Euclidiana\n2)Manhattan")
    nombreMetodo=input("Introduzca el numero del metodo a utilizar: \n")
    k=input("Introduce el valor de vecinos cercanos k: \n")
    knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,datoABuscar)

numDato=0

#nombreDatosBusqueda=input("Introduce el nombre del archivo de busqueda: \n")
#nombreDatosEntrenamiento=input("Introduce el nombre del archivo de entrenamiento: \n")

#datosBusqueda=LectorData.leerDatosBusqueda(nombreDatosBusqueda);
#datosEntrenamiento=LectorData.leerDatosEntrenamiento(nombreDatosEntrenamiento);

datosBusqueda=LectorData.leerDatosBusquedaP();
datosEntrenamiento=LectorData.leerDatosEntrenamientoP();

print("*-----------------------------------------Datos para búsqueda-----------------------------------------*")
for fila in datosBusqueda:
    print("No." + str(numDato) + " " + ", ".join(map(str, fila)))
    numDato = numDato + 1


datoABuscar=int(input("Escoga el numero de Dato que quiere Clasificar: \n"))   
print("Escoja El Metodo de Calculo de Distancias: \n1)Euclidiana\n2)Manhattan")
nombreMetodo=input("Introduzca el numero del metodo a utilizar: \n")
k=input("Introduce el valor de vecinos cercanos k: \n")
knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,datoABuscar)

opcion="a"
while(opcion!="s"):
    print("Escoga una opcion: \nc)Procesar El Siguiente Dato\nt)Procesar todos los datos de prueba\ns)Finalizar procesamiento")     
    opcion=input("")
    if opcion == "c":
        datoABuscar=datoABuscar+1
        knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,datoABuscar)
    elif opcion == "t":
        ejecucionKNN(datosBusqueda, datosEntrenamiento)
    elif opcion == "s":
        pass
    else:
        print("Opcion Introducida No Valida")

