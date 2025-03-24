import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPICO_M1 = "ALSI/Plaza Vea/Primavera/M1"
TOPICO_M2 = "ALSI/Plaza Vea/Primavera/M2"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT!")
        # Suscripción a ambos tópicos
        client.subscribe(TOPICO_M1)
        client.subscribe(TOPICO_M2)
    else:
        print(f"Error de conexión. Código: {rc}")

# Callback cuando recibe un mensaje
def on_message(client, userdata, msg):
    print(f"\nMensaje recibido [{msg.topic}]: {msg.payload.decode()}")

# Configurar cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker
client.connect(BROKER, PORT, 60)

# Mantener la conexión activa
print("Iniciando recepción de mensajes...")
client.loop_forever()