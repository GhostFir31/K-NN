class FilaTabla:
    
    def __init__(self, id,prediccion,realidad):
        self.id = id
        self.prediccion = prediccion
        self.realidad = realidad
        self.C0=""
        self.C1=""
        self.C2=""
        self.C3=""
        self.C4=""
        
    def MetodoTablaDeVerdad(self):
        clases = ["0", "1", "2", "3", "4"]
        resultados = [self.C0, self.C1, self.C2, self.C3, self.C4]

        for i, c in enumerate(clases):
            if self.realidad == c:
                if self.prediccion == self.realidad:
                    resultados[i] = "TP"
                else:
                    resultados[i] = "FN"
            else:
                if self.prediccion == c:
                    resultados[i] = "FP"
                else:
                    resultados[i] = "TN"

        self.C0, self.C1, self.C2, self.C3, self.C4 = resultados


                      
    def __str__(self):
        return "ID: " + str(self.id) + ", Prediccion: " + str(self.prediccion) + ", Realidad: " + str(self.realidad) + ", C0: " + str(self.C0) + ", C1: " + str(self.C1) + ", C2: " + str(self.C2) + ", C3: " + str(self.C3) + ", C4: " + str(self.C4)