import websocket

FORMAT_URL_CONNECTION_WEBSOCKETS = "ws://localhost:8888?id=%s"

def get_connection_to_machine_with_id(machine_id):
	ws = websocket.create_connection(FORMAT_URL_CONNECTION_WEBSOCKETS % (machine_id, ))
	return ws

def get_input_and_send_command_to_machine():
	machine_id = input('Enter machine id: ')
	ws = get_connection_to_machine_with_id(machine_id)
	command = input("Enter command: ")
	ws.send(command)
	ws.close()

if __name__ == "__main__":
	while True:
		get_input_and_send_command_to_machine()