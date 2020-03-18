"""The first step is to create an SMTP object, each object is used for connection
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)

# Next, log in to the server
# youremailaddress, password
server.login("") 

# send the mail
msg = "Hello" 
# The \n separates the  messages from the headers

# to send
# you@gmail.com, targetgmail.com
server.sendmail("ayushnegi369@gmaill.com", "ravindrasinghnegi9@gmail.com", msg)
