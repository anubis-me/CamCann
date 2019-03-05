from channels import Group


def ws_connect(message):
    print("WS connected")
    Group('data').add(message.reply_channel)
    message.reply_channel.send({"accept": True, })


def ws_disconnect(message):
    print("WS disconnected")
    Group('data').discard(message.reply_channel)