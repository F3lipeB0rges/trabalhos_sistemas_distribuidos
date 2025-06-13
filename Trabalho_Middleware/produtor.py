import pika
import psutil
import time

def obter_temperatura():
    temps = psutil.sensors_temperatures()
    if not temps:
        return 71.0  # valor fictício 
    for name, entries in temps.items():
        for entry in entries:
            if entry.current:
                return entry.current
    return 50.0

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='temperatura_cpu')

try:
    while True:
        temperatura = obter_temperatura()
        mensagem = f"{temperatura}"
        channel.basic_publish(exchange='', routing_key='temperatura_cpu', body=mensagem)
        print(f"[Produtor] Temperatura publicada: {mensagem}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Encerrando produtor.")
finally:
    connection.close()
