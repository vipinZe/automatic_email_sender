import smtplib

sender="Your Gmail Address"
password="Gmail App Password"

"List of receivers"
receivers=[
    "Recivers Gmail Address",
    "Recivers Gmail Address",
    "Recivers Gmail Address"

]
s= smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender, password)

message = """Subject: Test Email

Hello everyone, this is a test email.
"""

for email in receivers:
    print(f"Sending email to {email}...")
    s.sendmail(sender,email, message)
    print("Email sent successfully!")

s.quit()