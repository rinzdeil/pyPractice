from fpdf import FPDF
import glob

files = glob.glob("*.txt")
pdf = FPDF(orientation='P', format='A4')

for file in files:
    with open(file, 'r') as f:
        contents = f.read()
        # print(contents)

    title = file.strip('.txt').title()
    print(file, title)

    pdf.set_margins(20, 20, 30)

    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 20)
    pdf.cell(50, 10, txt=title, align='L', ln=1)
    pdf.set_font('Helvetica', '', 14)
    pdf.multi_cell(0, 7, txt=contents, align='L')

print("PDF Created")
pdf.output('animal_pages.pdf')


