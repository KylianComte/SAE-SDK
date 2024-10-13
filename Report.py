import reportlab 
import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.platypus import SimpleDocTemplate, Paragraph
class Report ():
    def __init__(self, nomtechnicien, filename, chemin_image, resultat) :
        self.nomtechnicien = nomtechnicien
        self.filename = filename
        self.pdf = canvas.Canvas(self.filename, pagesize=letter)
        self.width, self.height = letter
        self.titredoc = "Certificat de conformité"
        self.date = datetime.datetime.now().strftime("%d-%m-%Y / %H : %M")
        self.chemin_image = chemin_image
        self.resultat = resultat

    def title(self) :
        self.pdf.setFillColorRGB(255,0,0)
        self.pdf.setFont("Helvetica-Bold", 26)
        self.pdf.drawCentredString(self.width/2, self.height - 70, self.titredoc)

    def introduction(self):
        self.pdf.setFillColorRGB(0,0,255)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawString(self.width/14, self.height - 150, "Ce rapport a été rédigé le " + str(self.date)[:10] + " à " + str(self.date)[-7:])
        self.pdf.drawString(self.width/2, self.height - 150, "par le(s) technicien(s) " + self.nomtechnicien + ".")
        
    def content(self):
        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawString(self.width/14, self.height - 200,"Nom de l'instrument : " + str(self.resultat["name"]))
        self.pdf.drawString(self.width/14, self.height - 220,"Type d'instrument : " + str(self.resultat["type_instrument"]))
        self.pdf.drawString(self.width/14, self.height - 240,"Type de la mesure : " + str(self.resultat["type_mesure"]))
        self.pdf.drawString(self.width/14, self.height - 260,"Fréquence d'étude : " + str(self.resultat["f0"]))
        self.pdf.drawString(self.width/14, self.height - 280,"Résultat de la mesure : " + str(self.resultat["resultat"]))        
    
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
