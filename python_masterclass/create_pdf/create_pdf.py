import pandas as pd
from fpdf import FPDF

df = pd.read_csv('python_masterclass/create_pdf/pdf_topics.csv')

pdf = FPDF(orientation='P', unit='pt', format='A4')


def create_page(topic):
  pdf.add_page()
  pdf.set_font(family='Helvetica', style='B', size=24)
  pdf.set_text_color(100, 100, 100)
  pdf.cell(w=0, h=36, txt=topic, ln=1, border='B')


for index, row in df.iterrows():
  num_pages = int(row['Pages'])
  topic = row['Topic']

  for _ in range(num_pages):
    create_page(topic)

pdf.output('python_masterclass/create_pdf/output.pdf')

print('PDF created successfully!')
