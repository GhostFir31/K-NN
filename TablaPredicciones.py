class FilaTabla:
    
    def __init__(self, id,prediccion,realidad):
        self.id = id
        self.prediccion = prediccion
        self.realidad = realidad
        self.C0="FN"
        self.C1="FN"
        self.C2="FN"
        self.C3="FN"
        self.C4="FN"
        
    def MetodoTablaDeVerdad(self):
        if self.realidad == "0":
            if self.realidad == self.prediccion:
                self.C0 = "TP"
            else:
                self.C0 = "FN"
        elif self.realidad == "1":
            if self.realidad == self.prediccion:
                self.C1 = "TP"
            else:
                self.C1 = "FN"
        elif self.realidad == "2":
            if self.realidad == self.prediccion:
                self.C2 = "TP"
            else:
                self.C2 = "FN"
        elif self.realidad == "3":
            if self.realidad == self.prediccion:
                self.C3 = "TP"
            else:
                self.C3 = "FN"
        elif self.realidad == "4":
            if self.realidad == self.prediccion:
                self.C4 = "TP"
            else:
                self.C4 = "FN"
                      
    def __str__(self):
        return "ID: " + str(self.id) + ", Prediccion: " + str(self.prediccion) + ", Realidad: " + str(self.realidad) + ", C0: " + str(self.C0) + ", C1: " + str(self.C1) + ", C2: " + str(self.C2) + ", C3: " + str(self.C3) + ", C4: " + str(self.C4)