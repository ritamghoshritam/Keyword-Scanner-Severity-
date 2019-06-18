import time
import imaplib
def receive():
    time.sleep(20)
    msrvr=imaplib.IMAP4_SSL('imap.gmail.com',993)
    unm='hactelligence@gmail.com'
    pwd='1997Rg1997@'
    msrvr.login(unm,pwd)
    stat,cnt=msrvr.select('inbox')
    stat,dta=msrvr.fetch(cnt[0],'(UID BODY[TEXT])')
    x=dta[0][1]
    s=x.decode("utf-8")
    msrvr.close()
    msrvr.logout()
    if s.find('TRUE'):
        return True
    else:
        return False
 
'''
from datetime import datetime, timedelta
import email
from imapclient import IMAPClient

HOST = 'imap.gmail.com'
USERNAME = 'hactelligence'
PASSWORD = '1997Rg1997@'
ssl = True

today = datetime.today()
cutoff = today - timedelta(days=5)

## Connect, login and select the INBOX
server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)
select_info = server.select_folder('INBOX')

## Search for relevant messages
## see http://tools.ietf.org/html/rfc3501#section-6.4.5
messages = server.search(
    ['FROM', "sarthak.aggarwal1234@gmail.com",'SINCE',cutoff.strftime('%d-%b-%Y')])
response = server.fetch(messages,['RFC822'])

for msgid, data in response.items():
    msg_string = data[0][1]
    msg = email.message_from_bytes(msg_string)
    print ('ID %d: From: %s Date: %s' % (msgid, msg['From'], msg['date']))

'''
'''
import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('username@gmail.com', 'passwordgoeshere')
mail.list()
mail.select("INBOX") # connect to inbox.


result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, '(RFC822)')

raw_email = data[0][1]

email_message = email.message_from_string(raw_email)

print (email_message['Subject'])
'''
