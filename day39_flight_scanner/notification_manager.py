from twilio.rest import Client

TWILIO_SID = "AC3f28c8bad93d4c5e46be09d19781bc10"
TWILIO_AUTH_TOKEN = "854242cf29f21338ff07e4299faf0b99"
TWILIO_VIRTUAL_NUMBER = "+16107703071"
TWILIO_VERIFIED_NUMBER = "+972526839273"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
