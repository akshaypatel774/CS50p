from fpdf import FPDF

class Shirt:
    def __init__(self, name=None):
        self.name = name
        self.get_shirt()

    @classmethod
    def get_name(cls):
        name = input("Full name: ").strip()
        return cls(name)

    def get_shirt(self):
        pdf = FPDF(orientation="P", format="A4")
        pdf.add_page()

        # Print CS50 Shirtificate
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("helvetica", "B", 40)
        pdf.cell(0, 40, border=0, align="C", txt="CS50 Shirtificate")


        # Print <name> took CS50
        pdf.image("shirtificate.png", 10, 50, 190)
        pdf.ln()
        pdf.set_text_color(255, 255, 255)
        pdf.cell(5)
        pdf.set_font("helvetica", "B", 22)
        pdf.cell(0, 120, f"{self.name} took CS50", align="C")

        pdf.output("shirtificate.pdf")

def main():
    Shirt.get_name()


if __name__ == "__main__":
    main()