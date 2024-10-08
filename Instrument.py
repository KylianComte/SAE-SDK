import pyvisa

class Instrument (): 
    def __init__(self, name, type, adress) :
        self.name = name
        self.type = type
        self.addr = adress
        self.instrument = None

    def connect(self) :
        try :
            self.instrument = pyvisa.ResourceManager('@sim').open_resource(self.addr) # Name in sim librairy
            description = self.instrument.query('*IDN?')
        except :
            print("Erreur lors de la connexion, veuillez relancer le programme")
            exit()
        print("Instrument connecté avec succès !")
        print(description + " est prêt à être utilisé !")

    def preset(self) :
        pass


class Arv(Instrument) :
    def __init__(self, name, adress) :
        super().__init__(name, 'ARV', adress)

    def preset(self) :
        print(self.instrument.query('*RST'))

