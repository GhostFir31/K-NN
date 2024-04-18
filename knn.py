import TablaPredicciones
import LectorData
import MetodosDistancia
import csv

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
    
    ver=str(int(datoBusqueda[-1]))
      
    registrarDatosPrueba(ver,claseRepetidaMas)
    
    print("Prediccion: Clase "+str(claseRepetidaMas))
    print("Realidad: Clase "+ str(int(datoBusqueda[-1])))

def registrarDatosPrueba(datoBusqueda,claseRepetidaMas):
    global id
    fila = TablaPredicciones.FilaTabla(id,claseRepetidaMas,datoBusqueda)
    fila.MetodoTablaDeVerdad() 
    tablaVerdad.append(fila)
    id=id+1

def imprimirTablaVerdad():
    print("Tabla Verdad:")
    for fila in tablaVerdad:
        print(fila)

def registrarMatrizConfusion(tablaVerdad):

    for fila in tablaVerdad:
        claseReal = int(fila.realidad)
        clasePredicha = int(fila.prediccion)
        matrizConfusion[claseReal][clasePredicha] += 1
    
    print("Matriz de Confusion:")
    print("    C0 C1 C2 C3 C4")
    contadorfor=0
    for fila in matrizConfusion:
        print("C" + str(contadorfor) + ":" + str(fila))
        contadorfor=contadorfor+1

def ejecucionKNN(datosBusqueda,datosEntrenamiento):
    
    numDato=0
    print("*-----------------------------------------Datos para búsqueda-----------------------------------------*")
    for fila in datosBusqueda:
        print("No." + str(numDato) + " " + ", ".join(map(str, fila)))
        numDato = numDato + 1
       
    datoABuscar=int(input("Escoga el numero de Dato que quiere Clasificar: \n"))
    print("Escoja El Metodo de Calculo de Distancias: \n1)Euclidiana\n2)Manhattan")
    nombreMetodo=input("Introduzca el numero del metodo a utilizar: \n")
    k=input("Introduce el valor de vecinos cercanos k: \n")
    knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,datoABuscar)

def ejecucionTodosKNN(datosBusqueda,datosEntrenamiento):
    datoABuscar=0
    k=input("Introduce el valor de vecinos cercanos k: \n")
    for datoABuscar in range(len(datosBusqueda)-1):
        knn(datosBusqueda,datosEntrenamiento,"1",k,datoABuscar)
        
def crearArchivoTablaVerdad(tablaVerdad, filename='procesamientoDatosPrueba.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'prediccion', 'realidad', 'C0', 'C1', 'C2', 'C3', 'C4'])
        for fila in tablaVerdad:
            fila_list = [fila.id, fila.prediccion, fila.realidad,fila.C0,fila.C1,fila.C2,fila.C3,fila.C4]  
            writer.writerow(fila_list)

def crearArchivoMatrizConfusion(matrizConfusion, filename='matrizConfusion.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['C0', 'C1', 'C2', 'C3', 'C4'])
        for fila in matrizConfusion:
            writer.writerow(fila)
                        
def calcularMetricas(tablaVerdad):
    total = len(tablaVerdad)
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for fila in tablaVerdad:
        claseReal = int(fila.realidad)
        clasePredicha = int(fila.prediccion)
        
        if claseReal == clasePredicha:
            if claseReal == 1:
                tp += 1
            else:
                tn += 1
        else:
            if claseReal == 1:
                fn += 1
            else:
                fp += 1
                
    accuracy = (tp + tn) / total
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    fscore = 2 * (precision * recall) / (precision + recall)

    print("Precision:", precision)
    print("Recall:", recall)
    print("Accuracy:", accuracy)
    print("F-score:", fscore)
                   
id=1
numDato=0
tablaVerdad=[]
datoABuscar=0
matrizConfusion = [[0] * 5 for _ in range(5)]

#nombreDatosBusqueda=input("Introduce el nombre del archivo de busqueda: \n")
#nombreDatosEntrenamiento=input("Introduce el nombre del archivo de entrenamiento: \n")

#datosBusqueda=LectorData.leerDatosBusqueda(nombreDatosBusqueda);
#datosEntrenamiento=LectorData.leerDatosEntrenamiento(nombreDatosEntrenamiento);

datosBusqueda=LectorData.leerDatosBusquedaP()
datosEntrenamiento=LectorData.leerDatosEntrenamientoP()

print("a)Escoger un Dato para Clasificar\nb)Clasificar Todos los Datos de Prueba")
opcionMenu=input("")
if opcionMenu == "a":
    print("*-----------------------------------------Datos para búsqueda-----------------------------------------*")
    for fila in datosBusqueda:
        print("No." + str(numDato) + " " + ", ".join(map(str, fila)))
        numDato = numDato + 1  
    datoABuscar=int(input("Escoga el numero de Dato que quiere Clasificar: \n"))
    print("Escoja El Metodo de Calculo de Distancias: \n1)Euclidiana\n2)Manhattan")
    nombreMetodo=input("Introduzca el numero del metodo a utilizar: \n")
    k=input("Introduce el valor de vecinos cercanos k: \n")
    knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,datoABuscar)
elif opcionMenu == "b":
    ejecucionTodosKNN(datosBusqueda, datosEntrenamiento)
    imprimirTablaVerdad()


opcion="a"

while(opcion!="s"):
    print("Escoga una opcion: \nc)Procesar El Siguiente Dato\nt)Procesar todos los datos de prueba\ns)Finalizar procesamiento")     
    opcion=input("")
    if opcion == "c":
        if(datoABuscar>397):
            print("Dato Fuera del Limite")
        else:
            datoABuscar=datoABuscar+1
            knn(datosBusqueda,datosEntrenamiento,nombreMetodo,k,datoABuscar)
            imprimirTablaVerdad()
    elif opcion == "t":
        id=1
        tablaVerdad=[]
        ejecucionTodosKNN(datosBusqueda, datosEntrenamiento)
        imprimirTablaVerdad()
        datoABuscar=len(datosBusqueda)
    elif opcion == "s":
        registrarMatrizConfusion(tablaVerdad)
        crearArchivoTablaVerdad(tablaVerdad)
        crearArchivoMatrizConfusion(matrizConfusion)
        calcularMetricas(tablaVerdad)
    else:
        print("Opcion Introducida No Valida")

