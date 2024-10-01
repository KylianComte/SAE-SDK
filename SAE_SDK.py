# Script to run the SAE SDK
from .Mesure import*
from .Instrument import*
from .Report import*
from .Resultats import*

# Imports
import pyvisa

#0. Find instruments

def instrumentscan() :
    resourceManager = pyvisa.ResourceManager()
    print(resourceManager.list_resources())



### Main ###
instrumentscan()

