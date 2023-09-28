# import library
import math, random
import smtplib

# function to generate OTP
def generateOTP() :

	# Declare a digits variable
	# which stores all digits
	digits = "0123456789"
	OTP = ""

# length of password can be changed
# by changing value in range
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]

	return OTP

# Driver code
if __name__ == "__main__" :
	
	print("OTP of 4 digits:", generateOTP())
	
    sender = 'from@example.com'
    receivers = ['to@example.com']
    message = ("""From: From Person <from@example.com>
    To: To Person <to@example.com>
    Subject: OTP


    This is your OTP: {}
    """).format(generateOTP())

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print("Successfully sent email")
    except SMTPException:
        pass
