import reportlab 
import datetime
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.platypus import SimpleDocTemplate, Paragraph
class Report ():
    def __init__(self, nomtechnicien, filename, image) :
        self.nomtechnicien = nomtechnicien
        self.filename = filename
        self.pdf = canvas.Canvas(self.filename, pagesize=letter)
        self.width, self.height = letter
        self.titredoc = "Certificat de conformité"
        self.date = datetime.datetime.now().strftime("%d-%m-%Y / %H : %M")
        self.chemin_image = image

    def title(self) :
        self.pdf.setFillColorRGB(255,0,0)
        self.pdf.setFont("Helvetica-Bold", 26)
        self.pdf.drawCentredString(self.width/2, self.height - 70, self.titredoc)

    def introduction(self):
        self.pdf.setFillColorRGB(0,0,255)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawString(self.width/14, self.height - 150, "Ce rapport a été rédigé le " + str(self.date)[:10] + " à " + str(self.date)[-7:])
        self.pdf.drawString(self.width/2, self.height - 150, "par le technicien " + self.nomtechnicien + ".")
        
    def content(self):
        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawString(self.width/14, self.height - 200,"Nom de l'instrument : " + resultat["name"])
        self.pdf.drawString(self.width/14, self.height - 220,"Type d'instrument : " + resultat["type_instrument"])
        self.pdf.drawString(self.width/14, self.height - 240,"Type de la mesure : " + resultat["type_mesure"])
        self.pdf.drawString(self.width/14, self.height - 260,"Fréquence d'étude : " + resultat["f0"])
        self.pdf.drawString(self.width/14, self.height - 280,"Résultat de la mesure : " + resultat["resultat"])        
    
    def ajouter_image(self) : 
        self.pdf.drawImage(
            self.chemin_image, 
            self.width/6, 
            self.height - 670, 
            204*2, 
            153*2
            )
        
    def save(self):
        self.pdf.save()
        
    def create_pdf(self):
        self.title()
        self.introduction()
        self.content()
        self.save()

    def create_pdf_image(self):
        self.title()
        self.introduction()
        self.content()
        self.ajouter_image()
        self.save()

#Prog Principal     
resultat = {"name" : "ARV2", 
            "type_mesure" : "Coefficien de réflexion (S11)", 
            "type_instrument" : "ARV",
            "resultat" : "S11 = -25dB",
            "f0" : "1GHz"
            }

mondoc = Report("E", "Mesure.pdf", r"C:\Users\mar04\OneDrive\Images\chaine.jpg")
mondoc.create_pdf_image() 




num_taps = 51 # Il est utile d'utiliser un nombre impair de robinets.
cut_off = 3000 # Hz
sample_rate = 32000 # Hz

# créer notre filtre passe-bas
h = signal.firwin(num_taps, cut_off, fs=sample_rate)

# tracer la réponse impulsionnelle
plt.plot(h, '.-')
plt.show()