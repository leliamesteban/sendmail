import imaplib

gmail_user = 's3nd3m41L@gmail.com'
gmail_password = 'lapel status preamble petticoat cement'

try:
    server = imaplib.IMAP4_SSL('imap.google.com')
    server.login(gmail_user, gmail_password)
except Exception as exception:
    print(exception)
