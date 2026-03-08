# Email configuration
sender_email = "dev.test83299@gmail.com"  
sender_password = ""       # Place with your Gmail password
receiver_email = "saad29@somaiya.edu"
subject = "Test Email"
body = "This is a test email sent from Python."
smtp_server = "smtp.gmail.com"
smtp_port = 587 

import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login(sender_email, sender_password)
message = "Message_you_need_to_send second time"
s.sendmail(sender_email, receiver_email, message)
s.quit()
