import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass 

try:
    email = 'terkerenos@gmail.com'
    password = 'user123456789'
    send_to_email = 'gustiganes@gmail.com'
    subject = 'This is the subject'

    messagePlain = '1'
    jumlah = 5
                
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
 
except Exception as e:
    print("Something is wrong please Re-run this script!", e)
except KeyboardInterrupt:
    print("Terima Kasih")
  
