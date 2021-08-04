import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file with flatmates data such as flatmate name, days he stayed
    in the flat, period and a total amount of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image("files/house.png", w=30, h=30)
        pdf.set_font('Arial', 'B', 20)
        pdf.cell(0, 40, "Flatmates' bill " + bill.period, border=0, align='C', ln=1)
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 40, "Total amount: " + str(bill.amount), border=0, align='C', ln=1)
        pdf.set_font(family='Arial', size=14)
        pdf.cell(60, 25, flatmate1.name, border=0)
        pdf.cell(50, 25, str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)
        pdf.cell(60, 25, flatmate2.name, border=0)
        pdf.cell(50, 25, str(flatmate2.pays(bill, flatmate1)), border=0)

        pdf.output(f"files/{self.filename}", 'F')
        webbrowser.open(f"files/{self.filename}")
