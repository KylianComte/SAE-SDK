import pyvisa

class Instrument (): 
    def __init__(self, name, type, adress) :
        self.name = name
        self.type = type
        self.addr = adress
        self.instrument = None

    def connect(self) :
        try :
            self.instrument = pyvisa.ResourceManager('custom.yaml@sim').open_resource(self.addr) # Name in sim librairy
            description = self.instrument.query('*IDN?')
        except :
            print("Erreur lors de la connexion, veuillez relancer le programme")
            exit()
        print("Instrument connecté avec succès !")
        print(description + " est prêt à être utilisé !")

    def preset(self) :
        pass

    def calibration(self) :
        pass


class Arv(Instrument) :
    def __init__(self, name, adress) :
        super().__init__(name, 'ARV', adress)

    def preset(self) :
        print(self.instrument.query('*RST'))

    def calibration(self):
        #TODO : set frequencies (min, max, step)
        print("Avant de calibration, veuillez entrer les plages de vos mesures :")
        print("Fréquence minimale :(MHz)")
        fmin = int(input())
        print("Fréquence maximale :(MHz)")
        fmax = int(input())
        print("Pas de fréquence :(MHz)")
        fstep = int(input())
        #TODO : set power (ref, div)
        print("Puissance de référence :(dBm)")
        pref = int(input())
        print("Puissance par division :(dB)")
        pdiv = int(input())
        #TODO : set number of points
        print("Nombre de points :")
        n = int(input())


        print(self.instrument.query('!CAL'))
        
        print("Quelle calibration voulez-vous effectuer ?")
        print("1. Calibration x")
        print("2. Calibration x")
        print("3. Calibration x")
        
        #TODO : calibrate
        

