class NotificationService:

    @staticmethod
    def send_sms(number: str, message: str):

        return {
            "channel": "sms",
            "recipient": number,
            "message": message,
            "status": "queued"
        }

    @staticmethod
    def send_whatsapp(number: str, message: str):

        return {
            "channel": "whatsapp",
            "recipient": number,
            "message": message,
            "status": "queued"
        }

    @staticmethod
    def send_email(email: str, subject: str, message: str):

        return {
            "channel": "email",
            "recipient": email,
            "subject": subject,
            "message": message,
            "status": "queued"
        }