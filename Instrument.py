import pyvisa
import time

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
        if (description == "choo") :
            train = ["   _____                 . . . . . o o o o o","  __|[_]|__ ___________ _______    ____      o"," |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.","_|________|_[_________]_[________]_|__|________)<","  oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\ ","~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"]
            for line in train :
                print(line)
        else :
            print(description)
        input()


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
        
        print("Garder les valeurs par défaut ? (O/N)")
        keep = input()
        while (keep != 'O' and keep != 'N') :
            print("Entrée invalide : Veuillez entrer O ou N")
            keep = input()
        if (keep == 'N') :
            print("Veuillez preciser les plages de vos mesures :")
            print("Fréquence minimale :(MHz)")
            fmin = int(input())
            print("Fréquence maximale :(MHz)")
            fmax = int(input())
            print("Pas de fréquence :(MHz)")
            fstep = int(input())
            #TODO : set frequencies (min, max, step)
            
            print("Puissance de référence :(dBm)")
            pref = int(input())
            print("Puissance par division :(dB)")
            pdiv = int(input())
            #TODO : set power (ref, div)            
            
            print("Nombre de points :")
            n = int(input())
            #TODO : set number of points

        else :
            print("Valeurs par défaut conservées, appareil prêt à être calibré")

        
        print("Quelle calibration voulez-vous effectuer ?")
        print("1. Calibration Open Response")
        print("2. Calibration Short Response")
        print("3. Calibration Thru Response")
        print("4. Calibration Full 1 port")
        print("5. Calibration 1 path 2 port")
        choix = int(input())
        while (choix < 1 or choix > 5) :
            print("Entrée invalide : Veuillez choisir un nombre entre 1 et 5")
            choix = int(input())
        if (choix == 1) :
            print("Connecter l'open puis appuyer sur entrée")
            input()
            print(self.instrument.query('!CAL')) #TODO : check if it's the right command
        elif (choix == 2) :
            print("Connecter le short puis appuyer sur entrée (p1)")
            input()
            print(self.instrument.query('!CAL'))
        elif (choix == 3) :
            print("Connecter le thru puis appuyer sur entrée (p1)")
            input()
            print(self.instrument.query('!CAL'))
        elif (choix == 4) :
            print("Connecter l'open puis appuyer sur entrée (p1)")
            input()
            print("Connecter le short puis appuyer sur entrée (p1)")
            input()
            print("Connecter le load puis appuyer sur entrée (p1)")
            input()
            print(self.instrument.query('!CAL'))
        elif (choix == 5) :
            print("Connecter l'open puis appuyer sur entrée (p1)")
            input()
            print("Connecter le short puis appuyer sur entrée (p1)")
            input()
            print("Connecter le load puis appuyer sur entrée (p1)")
            input()
            print("Connecter le thru puis appuyer sur entrée (p1)")
            input()
            print(self.instrument.query('!CAL'))

        print("Calibration terminée")

