import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date


def generate_pdf(pair, score, regime, position, scenarios):
    os.makedirs("reports", exist_ok=True)
    file = f"reports/{pair}_Daily_FX_Note.pdf"
    c = canvas.Canvas(file, pagesize=A4)
    c.drawString(50, 800, f"Daily FX Note – {pair}")
    c.drawString(50, 770, f"Date: {date.today()}")
    c.drawString(50, 740, f"FX Score: {round(score, 2)}")
    c.drawString(50, 710, f"Regime: {regime}")
    c.drawString(50, 680, f"Recommended Position: {round(position, 2)}")
    c.drawString(50, 650, "Scenarios:")
    y = 620
    for _, row in scenarios.iterrows():
        c.drawString(60, y, f"{row['Scenario']}: {row['FX Move %']}%")
        y -= 20
    c.save()
