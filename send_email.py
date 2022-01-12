import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#The function sends an email with the summary report file, the sender is the MADA email
def send_mail():
	fromaddr = "madadocuments1@gmail.com"
	toaddr = "YOUR EMAIL" #Enter the receiver email address

	msg = MIMEMultipart()

	msg['From'] = fromaddr #Sender
	msg['To'] = toaddr #Reciever
	msg['Subject'] = "Summary Report" #Subject of the email

	body = "summary" #Body of the email

	msg.attach(MIMEText(body, 'plain'))

	filename = "summaryReport.txt"
	attachment = open(r"summaryReport.txt", "rb") #Attch the summary file 

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "mada12345")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

