import pyvisa

class Instrument (): 
    def __init__(self, name, type, adress) :
        self.name = name
        self.type = type
        self.ipaddr = adress
        self.instrument = None

    def connect(self) :
        self.instrument = pyvisa.ResourceManager().open_resource(self.ipaddr) # Name ?
        print(self.instrument.query('*IDN?'))

    def preset(self) :
        pass


class Arv(Instrument) :
    def __init__(self, name, adress) :
        super().__init__(name, 'ARV', adress)

    def preset(self) :
        self.instrument.write('*RST')

