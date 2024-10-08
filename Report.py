import reportlab 
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class Report ():
    def __init__(self, nomtechnicien, filename, titredoc, date) :
        self.nomtechnicien = nomtechnicien
        self.filename = filename
        self.pdf = canvas.Canvas(self.filename, pagesize=letter)
        self.width, self.height = letter
        self.titredoc = titredoc
        self.date = date

    def title(self) :
        self.pdf.setFillColor(255,0,0)
        self.pdf.setFont("Helvetica-Bold", 20)
        self.pdf.drawCentredString(self.width/2, self.height - 1, self.titredoc)

        self.pdf.setFillColor(0,0,0)
        self.pdf.setFont("Helvetica-Bold", 16)
        self.pdf.drawString(self.width/2, self.height - 50, self.nomtechnicien)

        self.pdf.setFillColor(0,0,255)
        self.pdf.setFont("Helvetica-Bold", 14)
        self.pdf.drawString(self.width/2, self.height - 100, self.date)


    def content(self):
        pass

    def save(self):
        self.pdf.save()

    def create_pdf(self, title, content):
       self.draw_header(title)
       self.draw_content(content)
       self.save()

mondoc = Report("Martin")
       

