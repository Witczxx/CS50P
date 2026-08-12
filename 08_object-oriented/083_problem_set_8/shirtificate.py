from fpdf import FPDF


class PDF(FPDF):

    def title_text(self, title):
        self.set_font("arial", style="B", size=48)
        self.cell(0, 60, title, align="C", ln=1)

    def shirt_text(self, text):
        self.set_font("arial", style="B", size=26)
        self.set_text_color(250, 250, 250)
        self.cell(0, 90, text, align="C", ln=1)
        self.cell(0, -55, "took CS50P", align="C", ln=1)


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image("shirtificate.png", (210 - 170) / 2, (297 - 170) / 2, 170, 170)

pdf.title_text("CS50P Shirtificate")
pdf.shirt_text(input("Enter your name: "))

pdf.output("shirtificate.pdf")

