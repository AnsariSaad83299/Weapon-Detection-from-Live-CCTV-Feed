import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def email():

    sender_email = "dev.test83299@gmail.com"
    receiver_email = "saad29@somaiya.edu"
    password = "" #enter ur password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  

    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Email with threat report"

    
    body = "This email has pdf threat report attached"
    message.attach(MIMEText(body, "plain"))

    
    pdf_filename = "temp/report.pdf"
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= report.pdf",
    )

    message.attach(part)

    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        
        server.login(sender_email, password)
        
        server.sendmail(sender_email, receiver_email, message.as_string())

    print('Email sent')

