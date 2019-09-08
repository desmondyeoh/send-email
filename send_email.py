"""
send_email method
"""

def send_email(username, password, sendto, subject, text):
    print("Sending Email to %s..." % sendto)
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    msg = 'Subject: {}\n\n{}'.format(subject, text)
    server.sendmail(username, sendto, msg)
    server.quit()
    print("Email sent!")