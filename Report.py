import reportlab 
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class Report ():
    def __init__(self, nomTechnicien, filename) :
        self.nomTechnicien = nomTechnicien
        self.filename = filename
        self.c = canvas.Canvas(self.filename, pagesize=letter)


    def setReport(self, report) :
        self.c.setFont("Helvetica-Bold", 16)
        self.c.drawString(100, self.height - 50, title)
    