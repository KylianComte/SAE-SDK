# Script to run the SAE SDK

# Imports
import pyvisa

#0. Find instruments

def instrumentscan() :
    resourceManager = pyvisa.ResourceManager()
    print(resourceManager.list_resources())


### Main ###
instrumentscan()

