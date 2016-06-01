from channels.sessions import channel_session
from channels import Group
from urllib.parse import urlparse, parse_qs
import pprint

pp = pprint.PrettyPrinter(indent=4)

@channel_session
def ws_connect(message):
	query_parameters = parse_qs(message.content['query_string'])
	machine_id = query_parameters['id'][0]
	Group(machine_id).add(message.reply_channel)
	message.channel_session['id'] = machine_id
	message.reply_channel.send({'text': 'In ws_connect'})

@channel_session
def ws_receive(message):
	print("In ws_receive")
	group = Group(message.channel_session['id'])
	message.reply_channel.send({'text': 'In ws_receive'})
	group.send({
		"text": message.content['text'],
	})

def ws_disconnect(message):
	print("In ws_disconnect")
	message.reply_channel.send({'text': 'In ws_disconnect'})