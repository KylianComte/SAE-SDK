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
                             "resultat" : str(self.mesure.result) + " dB",      # Resultat de S21
                             "f0" :  str(self.mesure.freq) + " MHz"              # A quelle freq
                            }
            
        if self.mesure.type == "Pertes de réflexion" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.mesure.type, 
                             "type_instrument" : self.instrument.type,
                             "resultat" : str(self.mesure.result) + " dB",
                             "f0" :  str(self.mesure.freq) + " MHz"
                            }

        if self.mesure.type == "Fréquence centrale" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.mesure.type,
                             "type_instrument" : self.instrument.type,
                             "resultat" : str(self.mesure.result) + " MHz",
                             "f0" :  None
                            }
            
        if self.mesure.type == "Bande passante 3dB" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.mesure.type,
                             "type_instrument" : self.instrument.type,
                             "resultat" : self.mesure.result,
                             "f0" :  None
                            }
        if self.mesure.type == "Bande passante 3dB" : 
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.mesure.type,
                             "type_instrument" : self.instrument.type,
                             "resultat" : self.mesure.result,
                             "f0" :  None
                            }
        
        if self.mesure.type[:20] == "Bande de réjection à" :
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.mesure.type,
                             "type_instrument" : self.instrument.type,
                             "resultat" : self.mesure.result,
                             "f0" :  None
                            }
        if self.mesure.type == "Sélectivité, facteur de forme" :
            self.resultat = {"name" : self.instrument.name, 
                             "type_mesure" : self.mesure.type,
                             "type_instrument" : self.instrument.type,
                             "resultat[1]" : self.mesure.result[0],
                             "resultat[2]" : self.mesure.reuslt[1],
                             "f0" :  None
                            }
        
            
     