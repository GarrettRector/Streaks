from twilio.rest import Client


def sendmessage(msg):
    account_sid = "TOKEN"
    auth_token = "TOKEN"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body=msg,
            from_='+NUMBER',
            to='+NUMBER'
        )
    print(message)
