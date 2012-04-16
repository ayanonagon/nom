from twilio.rest import TwilioRestClient

account = "AC6df70416da014a08ba197deda48ed274"
token = "625b6abc9ef179dd021cc4ebc374b0ad"
client = TwilioRestClient(account, token)
                                     
def send_notification_to(phone_number, message_text):
    message = client.sms.messages.create(to=phone_number, from_="+14155992671",
                                         body=message_text)

if __name__ == '__main__':
    send_notification_to('+12012483731', 'nom nom nom')
