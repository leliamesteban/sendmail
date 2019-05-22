import smtplib

# create insecure connection to ('server', port)
server = smtplib.SMTP('smtp.gmail.com', 587)
# identify to the server
server.helo()
