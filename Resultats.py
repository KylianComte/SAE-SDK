class Result ():
    def __init__(self, instrument, mesure) :
        self.instrument = instrument
        self.mesure = mesure
        self.resultat = None
    
    def formatResultat(self):
        if self.mesure.type == "Pertes d'insertion" : 
            self.resultat = {"name" : self.instrument.name,        # Nom de l'instrum
                             "type_mesure" : self.mesure.type, # S21
                             "type_instrument" : self.instrument.type, # ARV
                             "resultat" : self.mesure.result,      # Resultat de S21
                             "f0" :  self.mesure.freq              # A quelle freq
                            }
            
        if self.mesure.type == "Pertes de réflexion" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.results,
                             "f0" :  self.mesure.freq
                            }

        if self.mesure.type == "Fréquence centrale" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                             "f0" :  self.mesure.freq
                            }
            
        if self.mesure.type == "Bande passante 3dB" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                            }
        if self.mesure.type == "Bande passante 3dB" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                            }
        
        if self.mesure.type[:20] == "Bande de réjection à" :
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat" : self.mesure.result,
                            }
        if self.mesure.type == "Sélectivité, facteur de forme" :
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.instrument.type, 
                             "resultat[1]" : self.mesure.result[0],
                             "resultat[2]" : self.mesure.reuslt[1],
                            }
        
            
     