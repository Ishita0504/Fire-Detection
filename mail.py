import smtplib
def send_mail_function():

    recipientEmail = "Ishitabhadoria54@gmail.com"
    recipientEmail = recipientEmail.lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("ishitadeloitte05@gmail.com", 'zofr yzjy borg dvtg')
        server.sendmail('ishitadeloitte05@gmail.com', recipientEmail, "Warning A Fire Accident has been reported on ABC Company")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
    	print(e)
send_mail_function()