def send_sms(to: str, message: str) -> None:
    """Send an SMS message.

    Replace this implementation with the real SMS gateway integration.
    """
    print(f"Sending SMS to {to}: {message}")

send_sms(
    to="+27792652043",
    message="Electricity restoration underway in Ward 12"
)