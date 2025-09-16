import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

invoices_filepath = "python_masterclass/invoice_gen/invoices/"
excel_files = glob.glob(invoices_filepath + '*.xlsx')

for file in excel_files:
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  pdf.add_page()
  pdf.set_font(family='Helvetica', style='B', size=24)

  col_width = pdf.w / 5
  row_height = pdf.font_size * 1.5

  filepath = Path(file)
  filename = filepath.stem
  filename = filename.strip("002 ")
  invoice_num, date = filename.split("-")
  header = f"Invoice no.{invoice_num}"
  header_date = f"Date: {date}"

  pdf.cell(pdf.w / 2, row_height, txt=header)
  pdf.set_font(family='Helvetica', style='I', size=18)
  pdf.cell(0, row_height, txt=header_date, align='R', ln=1)

  df = pd.read_excel(file, sheet_name='Sheet 1')

  columns = [item.replace("_", " ") for item in df.columns]

  for i in range(len(columns)):
    pdf.set_font(family='Helvetica', style='B', size=10)
    pdf.cell(col_width, row_height, txt=columns[i], border=1, align='C')
  
  for index, row in df.iterrows():
    pdf.set_font(family='Helvetica', style='', size=8)
    pdf.cell(20, row_height, txt=str(row['product_id']), border=1, align='C')
    pdf.cell(70, row_height, txt=str(row['product_name']), border=1)
    pdf.cell(10, row_height, txt=str(row['amount_purchased']), border=1)
    pdf.cell(15, row_height, txt=str(row['price_per_unit']), border=1)
    pdf.cell(15, row_height, txt=str(row['total_price']), border=1)
    pdf.ln(row_height)
    
  #   print(index, row)
    # for item in row:
    #   print(item['product_id'])
    # print(type(item))
    # pdf.ln(row_height)

  pdf.output(f"python_masterclass/invoice_gen/{filename}.pdf")

# print(excel_files)
