class Measure ():
    def __init__(self) :
        self.instrument = None
        self.type = None
    
    def setInstrument(self, instrument) :
        self.instrument = instrument.instrument

    def getResults(self) :
        pass

class Pertes (Measure) :
    def __init__(self,frequence) :
        super().__init__()
        self.freq = frequence
        self.result = None

class PertesInsertion (Pertes) :
    def __init__(self,frequence) :
        super().__init__(frequence)
        self.type = "Pertes d'insertion"

    def getResults(self) :
        print("Mesure des pertes d'insertion à la fréquence " + str(self.freq) + "MHz")
        print("Mesure en cours...")
        print(self.instrument.query(f"!FREQ {self.freq}"))
        #TODO : measure S21
        self.result = float(self.instrument.query("?AMP"))
        print("Mesure terminée")


class PertesReflection (Pertes) :
    def __init__(self,frequence) :
        super().__init__(frequence)
        self.type = "Pertes de réflexion"

    def getResults(self) :
        print("Mesure des pertes de réflexion à la fréquence " + str(self.freq) + "MHz")
        print("Mesure en cours...")
        print(self.instrument.query(f"!FREQ {self.freq}"))
        #TODO : measure S11
        self.result = float(self.instrument.query("?AMP"))
        print("Mesure terminée")
        

class FrequenceCentrale (Measure) :
    def __init__(self) :
        super().__init__()
        self.type = "Fréquence centrale"
        self.result = None

    def getResults(self) :
        print("Mesure de la fréquence centrale")
        print("Mesure en cours...")
        fcent = 0 #TODO : measure frequence at max power
        print("Mesure terminée")
        self.result = fcent

class BandePassante (Measure) :
    def __init__(self) :
        super().__init__()
        self.type = "Bande passante 3dB"
        self.result = None

    def getResults(self) :
        print("Mesure de la bande passante 3dB")
        print("Mesure en cours...")
        maxpow = 0 #TODO : measure max power
        pow_3dB = maxpow - 3
        fmin = 0 #TODO : measure f-3dB min freq (at power = pow_3dB)
        fmax = 0 #TODO : measure f-3dB max freq (at power = pow_3dB)
        bp = fmax - fmin
        print("Mesure terminée")
        self.result = bp

class BandeRejet (Measure) :
    def __init__(self,rejection) :
        super().__init__()
        self.type = "Bande de réjection à " + str(rejection) + "dB"
        self.result = None
        self.rejection = rejection

    def getResults(self) :
        print("Mesure de la bande de réjection à " + str(self.rejection) + "dB")
        print("Mesure en cours...")
        maxpow = 0 #TODO : measure max power
        pow_reject = maxpow - self.rejection
        fmin = 0 #TODO : measure f-XdB min freq (at power = pow_reject)
        fmax = 0 #TODO : measure f-XdB max freq (at power = pow_reject)
        br = fmax - fmin
        print("Mesure terminée")
        self.result = br

class Selectivite_formfactor (Measure) :
    def __init__(self,rejection) :
        super().__init__()
        self.type = "Sélectivité, facteur de forme"
        self.rejection = rejection
        self.result = None

    def getResults(self) :
        print("Mesure de la sélectivité et le facteur de forme")
        mesbp = BandePassante()
        mesbp.getResults()
        bp = mesbp.result
        mesbr = BandeRejet(self.rejection)
        mesbr.getResults()
        br = mesbr.result
        selectivity = bp/br
        formfactor = br/bp
        print("Mesure terminée")
        self.result = [selectivity, formfactor]
