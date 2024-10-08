class Result ():
    def __init__(self, instrument, mesure, pert, resultat) :
        self.instrument = instrument
        self.mesure = mesure
        self.resultat = None
    
    def formatResultat(self):
        if str(self.mesure.type) == "Pertes d'insertion" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                             "f0" :  self.mesure.freq
                             }
            
        if str(self.mesure.type) == "Pertes de réflexion" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                             "f0" :  self.mesure.freq
                             }

        if str(self.mesure.type) == "Fréquence centrale" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                             "f0" :  self.mesure.freq
                             }
            
        if str(self.mesure.type) == "Bande passante 3dB" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                             }
        if str(self.mesure.type) == "Bande passante 3dB" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                             }
        
        if str(self.mesure.type[:20]) == "Bande de réjection à" :
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                             }
            
                
        