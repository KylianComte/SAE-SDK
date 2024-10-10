import reportlab 
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
import datetime

class Report ():
    def __init__(self, nomtechnicien, filename) :
        self.nomtechnicien = nomtechnicien
        self.filename = filename
        self.pdf = canvas.Canvas(self.filename, pagesize=letter)
        self.width, self.height = letter
        self.titredoc = "Certificat de conformité"
        self.date = datetime.datetime.now().strftime("%d-%m-%Y / %H : %M")

    def title(self) :
        self.pdf.setFillColorRGB(255,0,0)
        self.pdf.setFont("Helvetica-Bold", 26)
        self.pdf.drawCentredString(self.width/2, self.height - 70, self.titredoc)

        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.setFont("Helvetica-Bold", 14)
        self.pdf.drawCentredString(self.width/2, self.height - 100, self.nomtechnicien)

        self.pdf.setFillColorRGB(0,0,255)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawString(self.width/14, self.height - 150, "Ce rapport a été rédigé le " + str(self.date)[:10] + " à " + str(self.date)[-7:])

    def content(self):
        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawString(self.width/14, self.height - 180,"Nom de l'instrument : ")
        self.pdf.drawString(self.width/14, self.height - 200,"Mesure de l'instrument : " )

    def save(self):
        self.pdf.save()

    def create_pdf(self):
        self.title()
        self.content()
        self.save()
       
resultat = {"name" : "ARV2", 
            "type_mesure" : "Coefficien de réflexion (S11)", 
            "type_instrument" : "ARV",
            "resultat" : "S11 = 25dB",
            "f0" : "1GHz"
            }

mondoc = Report("Martin Russo & Kylian Comte", "Mesures.pdf")
mondoc.create_pdf()
       

