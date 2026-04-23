import smtplib

sender="Your email address"
password='Email app password'
reciever= "Reciver email address"


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender, password)
message = ("Hello, this is a test email. kese ho")
for x in range(2):
     print("Email: sending")
     
     s.sendmail(sender, reciever,message)
     print('email has been sent')
     
s.quit()
