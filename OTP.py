import pyotp
import time
#One Time Password implementation

#Create a new OTP object
key = pyotp.random_base32()
totp = pyotp.TOTP(key)

#Create a new token
first_token = totp.now()
print("This is the first token: ", first_token)

#Verify first token
status = totp.verify(first_token)
print("Is the first token valid?", status)
