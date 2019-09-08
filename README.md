# send-email
A simple Python method to send email

## Installation
1. Create a new GMail account just for this purpose (You may use your current GMail but not it's not recommended because it does not allow 2 Factor Authentication, and allow a non-browser to login. In other words, the email you will use for this purpose will be less secured).
2. Login to your new GMail account and go to, https://www.google.com/settings/security/lesssecureapps.
3. Switch "Allow less secure app" to be "ON".
![img](instruction-screenshot.png)
4. Find the Python method in [send_email.py] and use the method like so:
```
send_email("<YourNewGmailAccount@gmail.com>", "<YourNewGmailAccountPassword>", "ReceiverEmail@gmail.com", "Subject", "Body Text")
```
