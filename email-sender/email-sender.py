# steps: 1. go over your gmail acc and set up 2factor authetication
#generate app password 
# create a function to send the mail

from email.message import EmailMessage
from app2 import password 
import ssl 
import smtplib

email_sender = 'lferraznogueira@gmail.com'
email_password = password #here should be the password that google generated 
#i'll be putting in the tutorial to be more specific if you have any questions 

email_receiver = 'hageke7114@gam1fy.com' #you can go to google and look for tempmail to find one

subject = "Learning python"

body = """ 
Don't forget to keep learning. You're doing great!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)