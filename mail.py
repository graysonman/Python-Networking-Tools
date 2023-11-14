import smtplib
import ssl

from_email = ""  # Replace with your Gmail address
to_email = ""  # Replace with the recipient's email address
password = ""  # Replace with your Gmail password

msg = """\
Subject: I Love Computer Networks!

I love computer networks!
"""

smtp_server = "smtp.gmail.com"
port = 465

# Create a secure SSL context
context = ssl.create_default_context()

try:
    # Create a secure SMTP connection with Gmail's SMTP server
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg)

    print("Email sent successfully!")

except Exception as e:
    print(f"Error occurred: {e}")
