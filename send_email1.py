import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import os.path
print("""           ██████████████       ███████████          ████             ████            ████
           ██                   ██        ██        ██  ██            ██ ██          ██ ██ 
           ██                   ██        ██       ██    ██           ██  ██        ██  ██
           ██████████████       ███████████       ██████████          ██   ██      ██   ██
                       ██       ██               ██        ██         ██    ██    ██    ██
                       ██       ██              ██          ██        ██     ██  ██     ██
           ██████████████       ██             ██            ██       ██      ████      ██
""")
print("================== Created By alhassanAlharb7 ==================")
email=input("enter your gmail --> ")
password=input(str("enter the password for your email -->"))
send_email=input("enter the send email --> ")
subject=input("enter the subject --> ")
msg=MIMEMultipart()
msg['From']=email
msg['To']=send_email
msg['Subject']=subject
message=input("enter the message : ")
a=1
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("\033[0;31m [<>] message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))
while a==1:
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("message is sent")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        msg.attach(MIMEText('plain'))