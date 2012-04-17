from twilio.rest import TwilioRestClient

account = "REDACTED"
token = "REDACTED"
client = TwilioRestClient(account, token)
                                     
def send_notification_to(phone_number, message_text):
    message = client.sms.messages.create(to=phone_number, from_="+14155992671",
                                         body=message_text)

if __name__ == '__main__':
    send_notification_to('+somenumber', 'nom nom nom')
