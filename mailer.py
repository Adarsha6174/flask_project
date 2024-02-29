import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def SendMail(mail,messages):
        messages=str(messages)
        mail=str(mail)
        # Set up the email parameters
        sender_email ='20kq1a05a9@pace.ac.in'
        receiver_email = mail #0=mail,#1=message
        subject = "Subject of the email"
        message =messages

        # Create the email content
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to your email account
        server.login(sender_email, "pace1234")

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Quit the server
        server.quit()