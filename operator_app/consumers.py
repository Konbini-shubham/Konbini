def ws_connect(message):
	print(message)
	message.reply_channel.send({'text': 'In ws_connect'})

def ws_receive(message):
	print("In ws_receive")
	message.reply_channel.send({'text': 'In ws_receive'})

def ws_disconnect(message):
	print("In ws_disconnect")
	message.reply_channel.send({'text': 'In ws_disconnect'})