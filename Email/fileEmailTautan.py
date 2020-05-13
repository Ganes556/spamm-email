import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'gustiganes@gmail.com'
password = 'ghanes123456789'
send_to_email = 'ekajaya740@gmail.com'
subject = 'This is the subject'
messageHTML = '<p> INI PROGRESS KU <a href="https://drive.google.com/">drive/folders/1Q_bjeviE3hYYLQcClUGtLT_5HlcJFX22?usp=sharing<a><span style="color: #496dd0"> MAKASIH </span><p>'
messagePlain = 'INI KONTOL ANDA KAH HAHAHAH'

msg = MIMEMultipart('alternative')
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(messagePlain, 'plain'))
msg.attach(MIMEText(messageHTML, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
