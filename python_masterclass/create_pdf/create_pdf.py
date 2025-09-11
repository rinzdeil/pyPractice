import pandas as pd
from fpdf import FPDF

df = pd.read_csv('python_masterclass/create_pdf/pdf_topics.csv')

pdf = FPDF(orientation='P', unit='pt', format='A4')

def create_page(topic, page_num):
  pdf.add_page()
  pdf.set_font(family='Helvetica', style='B', size=24)
  pdf.set_text_color(100, 100, 100)
  pdf.cell(w=0, h=36, txt=f"{page_num}. " + topic, ln=1, border='B')

  for x in range(42):
    pdf.cell(w=0, h=16, txt='', ln=1, border='B')

def footer():
  current_page = pdf.page_no()
  total_pages = len(df)
  pdf.ln(10)
  pdf.set_font(family='Helvetica', style='I', size=12)
  pdf.set_text_color(100, 100, 100)
  pdf.cell(w=0, h=10, txt=f'p. {current_page}/{total_pages}', align='R')

for index, row in df.iterrows():
  pages = int(row['Pages'])
  page_num = int(row['Order'])
  topic = row['Topic']

  for i in range(pages):
    create_page(topic, page_num)
    footer()

pdf.output('python_masterclass/create_pdf/output.pdf')

print('PDF created successfully!')
