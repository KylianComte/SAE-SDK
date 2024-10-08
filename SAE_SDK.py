# Script to run the SAE SDK

#from .Report import Report
#from .Resultats import Resultats

# Imports
import time
import pyvisa
from Instrument import Instrument, Arv
from Mesure import Measure, Pertes, PertesInsertion, PertesReflection, FrequenceCentrale, BandePassante, Selectivite_formfactor, BandeRejet


#0. Find instruments

def instrumentscan() :
    resourceManager = pyvisa.ResourceManager('custom.yaml@sim')
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

print("Préparation de l'instrument...")
instrument.preset()
print("L'instrument est prêt à être calibré")
print("Appuyez sur entrée pour continuer")
input()
instrument.calibration()
print("Calibration terminée")
print("Appuyez sur entrée pour continuer")
input()
print("Quelle mesure voulez-vous effectuer ?")
print("1. Fréquence centrale")
print("2. Pertes d'insertion (S21)")
print("3. Bande passante 3dB")
print("4. Bande de rejection à XXdB")
print("5. Séléctivité, facteur de forme")
print("6. Pertes par reflexion (S11)")

choix = int(input())
while (choix < 1 or choix > 6) :
    print("Entrée invalide : Veuillez choisir un nombre entre 1 et 6")
    choix = int(input())

if (choix == 1) :
    mesure = FrequenceCentrale()
    mesure.getResults()
if (choix == 2) :
    frequence = int(input("Entrez la fréquence de mesure (MHz)"))
    mesure = PertesInsertion()
    mesure.getResults()
if (choix == 3) :
    mesure = BandePassante()
    mesure.getResults()
if (choix == 4) :
    rejet = int(input("Entrez la valeur de rejet (dB)"))
    mesure = BandeRejet(rejet)
    mesure.getResults()
if (choix == 5) :
    rejet = int(input("Entrez la valeur de rejet (dB)"))
    mesure = Selectivite_formfactor(rejet)
    mesure.getResults()