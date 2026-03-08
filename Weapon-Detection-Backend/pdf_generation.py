# # importing modules
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import datetime
import os

def pdf():
    fileName = 'temp/report.pdf'
    documentTitle = 'sample'
    title = 'Alert!!!'
    subTitle = 'Threat report generated......'
    current_date = datetime.date.today()

    current_time = datetime.datetime.now().time()

    formatted_date = current_date.strftime("%Y-%m-%d")
    formatted_time = current_time.strftime("%H:%M:%S")
    textLines = [
        'Mumbai',
        formatted_date,
        formatted_time
        ]

    pdf = canvas.Canvas(fileName, pagesize=letter)

    pdf.setTitle(documentTitle)

    
    pdf.setFont('Helvetica', 36)
    pdf.drawCentredString(300, 700, title)

    
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 650, subTitle)

    pdf.line(30, 640, 550, 640)

  
    text = pdf.beginText(40, 600)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)

    for line in textLines:
        text.textLine(line)

    pdf.drawText(text)

    files_in_temp = os.listdir('temp')

    imgs = []
    img_count = 0
    while img_count < 5:
        imgs.append('temp/'+ files_in_temp[img_count])
        img_count += 1

    img_height = 300
    img_width = 400

    y = 500 - img_height

    for image in imgs:
        if y < 0 :
            pdf.showPage()
            y = 800 - (img_height + 20)  

        pdf.drawImage(image, x=100, y=y, width= img_width, height=img_height)

        y -= (img_height + 20) 

    # Save the PDF
    pdf.save()

    print('pdf generated and saved')
