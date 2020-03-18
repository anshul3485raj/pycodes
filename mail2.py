"""Python script to send mail 
using your Gmail account"""

# importing SMTP module
import smtplib

# create an SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# starts TLS for security
s.starttls()

# Authentication
s.login('ayushnegi369@gmail.com', 'ayu123#345')

# message to be sent
message = "Hello I'm Ayush Negi :)"

# sending the mail
s.sendmail('ayushnegi369@gmail.com', 'ravindrasinghnegi9@gmail.com', message)

# terminating the session 
s.quit()
