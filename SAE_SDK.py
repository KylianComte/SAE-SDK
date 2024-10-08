# Script to run the SAE SDK

#from .Mesure import Measure
#from .Report import Report
#from .Resultats import Resultats

# Imports
import time
import pyvisa
from Instrument import Instrument, Arv


#0. Find instruments

def instrumentscan() :
    resourceManager = pyvisa.ResourceManager('@sim')
    return resourceManager.list_resources()



### Main ###
print("Bienvenue dans le SAE SDK")
print("Programme créé par RUSSO Martin et COMTE Kylian")
print("Pour commencer, veuillez brancher les instruments et appuyer sur entrée")
input()
print("Recherche des instruments...")
ListeInstruments = instrumentscan()
print("Instruments trouvés :")
for i in range(len(ListeInstruments)) :
    print(f'{i}. {ListeInstruments[i]}')

print("Veuillez choisir l'instrument à utiliser (entrez un nombre entre 0 et " + str(len(ListeInstruments)-1) + ")")

no_instrument = int(input())
while (no_instrument < 0 or no_instrument >= len(ListeInstruments)) :
    print("Entrée invalide : Veuillez choisir un nombre entre 0 et " + str(len(ListeInstruments)-1))
    no_instrument = int(input())

print("Vous avez choisi l'instrument " + ListeInstruments[no_instrument])
print("L'instrument est-il un ARV ? (O/N)")
is_arv = input()
while (is_arv != 'O' and is_arv != 'N') :
    print("Entrée invalide : Veuillez entrer O ou N")
    is_arv = input()
if (is_arv == 'O') :
    print("Nommez l'instrument")
    nom_instrument = input()
    instrument = Arv(nom_instrument, ListeInstruments[no_instrument])
else :
    print("Type d'instrument non pris en compte, modifiez le programme")
    exit()

print("Connexion à l'instrument...")
instrument.connect()
time.sleep(1)
instrument.preset()