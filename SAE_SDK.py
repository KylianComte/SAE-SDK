# Script to run the SAE SDK

#from .Mesure import Measure
#from .Instrument import Arv
#from .Report import Report
#from .Resultats import Resultats

# Imports
import pyvisa


#0. Find instruments

def instrumentscan() :
    resourceManager = pyvisa.ResourceManager('@sim')
    print(resourceManager.list_resources())



### Main ###
instrumentscan()

