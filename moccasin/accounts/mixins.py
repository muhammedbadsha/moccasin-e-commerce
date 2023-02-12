from django.conf import settings 
from twilio.rest import Client
import random




class MssageHandler:
    phone_number = None
    otp = None
    def __init__(self,phone_number,otp):
        self.phone_number = phone_number
        self.otp = otp
        print(otp)
        print(settings.ACCOUNT_SID)

    def send_otp_to_phone(self):
        # try:
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
        print('please waite')
        message = client.messages.create(
            body =f'your OTP is {self.otp}',
            from_=settings.TWILIO_NUMBER,
            to= '+91'+ self.phone_number,
        )
        print(message.body)
        # except:
        #     pass