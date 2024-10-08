import reportlab 
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class Report ():
    def __init__(self, nomtechnicien, filename, titredoc, date, resultat) :
        self.nomtechnicien = nomtechnicien
        self.filename = filename
        self.pdf = canvas.Canvas(self.filename, pagesize=letter)
        self.width, self.height = letter
        self.titredoc = titredoc
        self.date = date
        self.resultat = resultat

    def title(self) :
        self.pdf.setFillColorRGB(255,0,0)
        self.pdf.setFont("Helvetica-Bold", 26)
        self.pdf.drawCentredString(self.width/2, self.height - 70, self.titredoc)

        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.setFont("Helvetica-Bold", 14)
        self.pdf.drawCentredString(self.width/2, self.height - 100, self.nomtechnicien)

        self.pdf.setFillColorRGB(0,0,255)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawCentredString(self.width/2, self.height - 120, self.date)

    def content(self):
        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.setFont("Helvetica-Bold", 12)
        self.pdf.drawText(f"Nom de l'instrument : " {self.resultat.result["1"]})
        self.pdf.drawText(f"Mesure de l'instrument : " {self.resultat.result["2"]})
        

    def save(self):
        self.pdf.save()

    def create_pdf(self):
       self.title()
       self.save()

mondoc = Report("Martin Russo & Kylian Comte", "Mesures.pdf", "Rapportd de mesure", "08/10/2024")
mondoc.create_pdf()
       

