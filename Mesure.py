class Measure ():
    def __init__(self) :
        self.instrument = None
        self.type = None
    
    def setInstrument(self, instrument) :
        self.instrument = instrument

    def getResults(self) :
        pass

class Pertes (Measure) :
    def __init__(self,frequence) :
        super().__init__()
        self.freq = frequence
        self.result = None

class PertesInsertion (Pertes) :
    def __init__(self,frequence) :
        super().__init__(frequence)
        self.type = "Pertes d'insertion"

    def getResults(self) :
        print("Mesure des pertes d'insertion à la fréquence " + str(self.f) + "MHz")
        print("Mesure en cours...")
        #TODO : measure
        print("Mesure terminée")
        print("Appuyez sur entrée pour continuer")
        input()
        #TODO : return results = self.result

class PertesReflection (Pertes) :
    def __init__(self,frequence) :
        super().__init__(frequence)
        self.type = "Pertes de réflexion"

    def getResults(self) :
        print("Mesure des pertes de réflexion à la fréquence " + str(self.f) + "MHz")
        print("Mesure en cours...")
        #TODO : measure
        print("Mesure terminée")
        print("Appuyez sur entrée pour continuer")
        input()
        

class Parametres (Measure) :
    def __init__(self)