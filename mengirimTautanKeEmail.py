import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass 

try:
    email = input('your email: ')
    password = getpass('your password: ')
    send_to_email = input('email_to_send: ')
    subject = 'This is the subject'

    messagePlain = input('pesan: ')
    jumlah = int(input('Jumlah Pesan: '))
                
    msg =MIMEMultipart('alternative')
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(messagePlain, 'plain'))


    for x in range(0,jumlah):
            
        print("Number of Message Sent : " , x+1)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
    server.quit()
    print ("successfully sent email to %s:" % (msg['To']))   
 
except Exception:
    print("Something is wrong please Re-run this script!")
except KeyboardInterrupt:
    print("Terima Kasih")
  
    

