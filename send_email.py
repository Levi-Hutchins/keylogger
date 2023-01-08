import os
from email.message import EmailMessage
import ssl
import smtplib

sender = "ofingy101@gmail.com"
secret = "bqbdrxoeupkiasab"
reciever = "ofingy101@gmail.com"

subject = "TESt"
body = """
Helo levi

"""

em = EmailMessage()
em['From'] = sender
em['To'] = reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender,secret)
    smtp.sendmail(sender,reciever,em.as_string())