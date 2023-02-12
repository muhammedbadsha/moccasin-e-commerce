import os
from requests import request
from twilio.rest import Client
from moccasin.settings import ACCOUNT_SID,AUTH_TOKEN,SERVICE_SID

def verify(phone_number):
      account_sid = ACCOUNT_SID
      # Your Auth Token from twilio.com/console
      auth_token  = AUTH_TOKEN
      # print(TWILIO_NUMBER)
      client = Client(account_sid, auth_token)
      verification = client.verify \
                     .services(SERVICE_SID) \
                     .verifications \
                     .create(to='+91'+ phone_number, channel='sms')
      print(verification.sid)

def verify_check(phone_number,otp):
      account_sid = ACCOUNT_SID
      auth_token = AUTH_TOKEN
      client = Client(account_sid, auth_token)
      verification_check = client.verify \
                           .services(SERVICE_SID) \
                           .verification_checks \
                           .create(to='+91'+ phone_number, code=otp)
      print(verification_check.status)
      if verification_check.status=="approved":
       return True
      else:
       return False 