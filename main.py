from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', format='a4', unit="mm")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for _, row in df.iterrows():

    for n in range(row['Pages']):

        pdf.add_page()

        if n == 0:
            pdf.set_text_color(100,100,100)
            pdf.set_font(family='Times', style='B', size=24)
            pdf.cell(w=0, h=24, txt=row['Topic'])
            pdf.set_draw_color(100,100,100)
            # pdf.line(10, 30, 200, 30)
        for i in range(26):
            pdf.line(10, 30 + i * 10, 200, 30 + i * 10)
        pdf.ln(270)
        pdf.set_text_color(200,200,200)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')


pdf.output('output.pdf')
