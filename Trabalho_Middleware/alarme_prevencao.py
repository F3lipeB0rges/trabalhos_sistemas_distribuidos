import pika
import os

def alarme_callback(ch, method, properties, body):
    print(f"[Alarme] 🚨 {body.decode()}")
    os.system('echo -e "\a"') 

def prevencao_callback(ch, method, properties, body):
    print(f"[Prevenção] 🔧 {body.decode()}")

conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexao.channel()

canal.queue_declare(queue='alarme_incendio')
canal.queue_declare(queue='ativar_prevencao')

canal.basic_consume(queue='alarme_incendio', on_message_callback=alarme_callback, auto_ack=True)
canal.basic_consume(queue='ativar_prevencao', on_message_callback=prevencao_callback, auto_ack=True)

print('[Alarme/Prevenção] Aguardando mensagens de alerta...')
canal.start_consuming()
