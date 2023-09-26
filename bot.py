import random
def handle_response(msg):
    p=msg.lower()
    if p=="hello":
        return "hey there"
    if p=="roll":
        return str(random.randint(1,6))
    if p=="?us":
        return "get merried"

