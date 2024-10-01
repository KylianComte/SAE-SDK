# Script to run the SAE SDK
#1. Design instrument
#2. Run instrument for measure M
#3. Display results

# Imports
import pyvisa

#0. Find instruments

def instrumentscan() :
    resourceManager = pyvisa.ResourceManager()
    print(resourceManager.list_resources())

#1. Design instrument

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

#2. Run instrument for measure M

class Result ():
    def __init__(self) :
        pass

class Report ():
    def __init__(self) :
        pass

    def setReport(self, report) :
        pass

class Measure ():
    def __init__(self) :
        pass
    
    def getResults(self) :
        pass

### Main ###
resourceManager = pyvisa.ResourceManager()
print(resourceManager.list_resources())
