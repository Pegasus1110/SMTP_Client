import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.mail.yahoo.com.', 465)

server.ehlo()

server.login('pegasus_047@yahoo.com', 'otbgxxasofgtbeeq')

msg = MIMEMultipart()
msg['From'] = 'SMTP_SERVER_Tanishq Agarwal'
msg['To'] = 'mibrvfpzuqbltyvawx@kvhrr.com'
msg['Subject'] = 'Just a test Subject'
msg.attach(MIMEText("Hello my name is Tanishq.", 'plain'))

filename = 'test.jpg'
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment;filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('pegasus_047@yahoo.com', 'mibrvfpzuqbltyvawx@kvhrr.com', text)
