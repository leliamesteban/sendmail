import smtplib

sender = 's3nd3m41L@gmail.com'
gmail_user = 's3nd3m41L@gmail.com'
gmail_password = 'lapel status preamble petticoat cement'
to = 's3nd3m41L@gmail.com'
subject = ''
body = ''

email = """\
From: {}
To: {}
Subject: {}
{}
""".format(sender, to, subject, body)

try:
    # create secure (TLS/SSL) connection to ('server', port)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user, gmail_password)
    server.sendmail(sender, to, email)
except Exception as exception:
    print(exception)
finally:
    server.close()
