# send-email
A simple Python method to send email.
You can use this Python method

## Installation
1. Create a new GMail account just for this purpose (You may use your current GMail but not it's not recommended because you will need to turn off 2 Factor Authentication, which makes your account less secure).
2. Login to your new GMail account and go to, https://www.google.com/settings/security/lesssecureapps.
3. Toggle "Allow less secure apps" to be "ON":
![img](instruction-screenshot.png)
4. Find the Python method in [send_email.py] and use the method like so:
```
send_email("YourNewEmail", "YourNewEmailPassword", "ReceiverEmail", "EmailTitle", "EmailBody")
```
