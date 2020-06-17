#!/usr/bin/python

import smtplib

sender = 'ramagirividya03@gmail.com'
receivers = ['vidyaramagiri38@gmail.com']

message = """From: From Person <ramagirividya03@gmail.com>
To: To Person <vidyaramagiri38@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
