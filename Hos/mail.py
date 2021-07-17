import time
import datetime
import smtplib

def msgs():
	gmailaddress = 'rao794385@gmail.com'
	gmailpassword = 'Ravirao@123'
	mailto = '2017bcs080@sggs.ac.in'
	SUBJECT = 'Approved appointment'
	msg = 'Your appointment is approved'
	message = 'Subject:{}\n\n{}'.format(SUBJECT,msg)
	mailServer = smtplib.SMTP('smtp.gmail.com',587)
	mailServer.starttls()
	mailServer.login(gmailaddress, gmailpassword)
	mailServer.sendmail(gmailaddress,mailto,message)
	print("\nSend!!")
	mailServer.quit()