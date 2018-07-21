import smtplib
fromaddr="abc@gmail.com"               # for example
toaddr="xyz@gmail.com"                 # for example
message="hi!"
password="abc0009"                     # for example
server=smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(fromaddr, password)
server.sendmail(fromaddr, toaddr, message)
print("success")
server.quit()
