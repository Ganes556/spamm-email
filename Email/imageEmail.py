# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

messageHTML = messageHTML = '<p> Ini tugas saya <b> I Gusti Agung Ganes Satsangga Dipa </b> kelas <b>XI MIPA 8</b> absen <b>11</b> </p>'
# create message object instance
msg = MIMEMultipart()
 
 
# setup the parameters of the message
password = 'ghanes123456789'
msg['From'] = "gustiganes@gmail.com"
msg['To'] = "ghanes556@gmail.com"
msg['Subject'] = "Photo Tugas Bing Wajib"
 
# attach image to message body
msg.attach(MIMEImage(file("D:\Tugas Bing.jpg").read()))
msg.attach(MIMEImage(messageHTML,'html'))
 
# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
