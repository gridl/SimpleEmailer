import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import imaplib

#Read Mail

def read():
    os.system("cls")
    mailserver = imaplib.IMAP4_SSL('imap.aol.com',993)
    username = 'uname'
    password = 'pwd'
    mailserver.login(username, password)
    status, count = mailserver.select('Inbox')
    status, data = mailserver.fetch(count[0],'(UID BODY[TEXT])')
    print data[0][1]
    mailserver.close()
    mailserver.logout()
    choice = raw_input("Press x to clear screen:  ")
    if choice == "x":
        os.system("cls")




#Send Mail
def send():
    fromaddr = 'email@aol.com'
    toaddr = raw_input("Enter recievers email address: ")
    subject = raw_input("Enter the subject: ")
    text = raw_input("Enter the message: ")
    username = 'uname'
    password = 'pwd!'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Test'
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.aol.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr,toaddr,msg.as_string())
    server.quit()
    choice = raw_input("Email Sent. Press x to clear: ")
    if choice == "x":
        os.system("cls")
while 1:
    os.system("cls")
    print("Email Program")
    print("--------------")
    print("1. Read Email")
    print("2. Send Email")
    print("3. Exit")
    choice = raw_input("Enter choice: ")
    if choice == "1":
       read()
    elif choice == "2":
       send()
    elif choice == "3":
       break;
            
        
        
        

    