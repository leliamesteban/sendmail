import smtplib

# create secure (TLS/SSL) connection to ('server', port)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
