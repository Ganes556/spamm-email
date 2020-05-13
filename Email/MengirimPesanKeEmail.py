import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'ghanes@gmail.com' #pengirim
password = 'ghanes1234'   
send_to_email = 'ghanes556@gmail.com' #tujuan email
subject = 'This is the subject' #subject dalam email
message = 'hai'
file_location ="E:\Html Try\Kontak\TextLatihan.htm" 

msg = MIMEMultipart()
msg['From']=email
msg['To']= send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message,'plain'))#pesan yang dibawa brupa plain

filename = os.path.basename(file_location)
lampiran = open(file_location,"rb")
part = MIMEBase('application', 'Perkenalan')#perkenalan sebagai argumen string
part.set_payload((lampiran).read())#menyampaikan file yg bru di baca
encoders.encode_base64(part)#menyandikan object dengan base64
part.add_header('Content-MyFile',"lampiran; filename= %s" % filename)#declare lampiran dan penyedia filename

msg.attach(part)#melampirkan object yang sebelumnya tlah di buat

server = smtplib.SMTP('smtp.gmail.com',587)#mengubungi server 
server.starttls()#memulai keamanan gmail TLS
server.login(email,password)
text = msg.as_string() # memberi nama menjadi text
server.sendmail(email , send_to_email , text)
server.quit() 
