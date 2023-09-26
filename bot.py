import random

def handle_response(msg):
    # Convert the message to lowercase for case-insensitive comparison
    msg_lower = msg.lower()
    if msg_lower == "hello":
        return "Hey there"
    elif msg_lower == "roll":
        return str(random.randint(1, 6))
    elif msg_lower == "?us":
        return "get married"
    else:
        return "ez the code,free ur mood :)"+msg_lower
