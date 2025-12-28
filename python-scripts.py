# single Recipent
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
  # Email settings
  sender_email = 'sundeep.reddy@gmail.com'
  sender_password = 'send this message'

  # Create email message
  msg = MIMEText(body)
  msg['subject'] = subject
  msg['From'] = sender_email
  msg['To'] = to_email

  # Sending email
  with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server.login(sender_email, sender_password)
    server.sendemail(sender_email, to_email, msg.as_string())

  # Example usage:
  send_email('Automation Test', 'This is an automated message.','sundeep.reddy@gmail.com')
