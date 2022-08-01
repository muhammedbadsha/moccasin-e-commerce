from ast import excepthandler
from logging import exception
from django.conf import settings
from twilio.rest import Client
import random


   


def send_otp_to_phone(phone_number):
    try:
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
        
        
        message = client.verify \
                     .services(settings.SERVICE_SID) \
                     .verifications \
                     .create(from_='+15715203190',to='+91'+ phone_number, channel='sms')
        
    except :
        pass