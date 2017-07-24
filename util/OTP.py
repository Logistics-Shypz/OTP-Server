import random
import hashlib
import pyotp
import urllib
import urllib2


class OTP:

    #defining class variable
	__otpcounter=0
	

	def __init__(self):
		OTP.__otpcounter += 1
		r_base = pyotp.random_base32()
		self.shypz_hotp = pyotp.HOTP(r_base)

	def sendOTP(self):
		print "hello"

	def getGlobalOTPCount(self):
		return "OTP Count is : %d" % OTP.__otpcounter

	def generateOTP(self):
		return random.randrange(100000,999999,1)

	def generateOTP_v2(self,mobile):
		#shypz_hotp = pyotp.HOTP(r_base)
		#otp = shypz_hotp.at(int(mobile))
		otp = self.shypz_hotp.at(int(mobile))
		return otp
		#print otp
		#print shypz_hotp.verify(otp,int(mobile))
    
	def verifyOTP(self,otp,mobile):
		return self.shypz_hotp.verify(otp,int(mobile))
#Algorithm to generate OTP
#when the user do signup the otp gets generated aand gets deliver to user on mobile.
#user then will enter the otp in mobile or on website to pass the authentication




# otp1 = OTP()
# ot1 = otp1.generateOTP_v2('9739325635')
# v1 = otp1.verifyOTP(ot1,'9739325635')
# print v1

# otp2 = OTP()
# ot2 = otp2.generateOTP_v2('9619028595')
# v2 = otp2.verifyOTP(ot2,'9619028595')
# print v2

# print ot1
# print ot2

# print otp2.getGlobalOTPCount()


#otp1.sendOTP("anubhav","9739325635")
#str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#ls = random.sample(str,6)

#optstr=''

#for i in ls:
#	optstr += i
#print optstr
#hash_object = hashlib.sha1(optstr)
#hex_dig = hash_object.hexdigest()
#print(hex_dig)