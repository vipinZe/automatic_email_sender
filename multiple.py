import smtplib

sender="vipin4239thakur@gmail.com"
password="sjci bfzp uyed ziow"

"List of receivers"
receivers=[
    "deeyadav1818@gmail.com",
    "vip3956in@gmail.com",
    "rahulprajapati543ak@gmail.com"
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