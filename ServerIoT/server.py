from paho.mqtt import client as mqtt_client

#Brocker info
broker = '10.0.41.165'	# broker ip
port = 9001 # 9001 or 1883

#Client-Server info
my_topics = [
	('game/data', 1),
	('instructions', 1)
]
client_id = f'publish-{999}' # generate this


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(my_topics)
    print(0)


def client_forever():

	client = mqtt_client.Client()
	client.on_connect = on_connect

	client.connect(broker, port, 60)
	client.loop_forever()



if __name__ == "__main__":  
    client_forever()