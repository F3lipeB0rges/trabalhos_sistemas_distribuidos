import pika

LIMITE = 70.0

def callback(ch, method, properties, body):
    temperatura = float(body.decode())
    print(f"[Detector] Temperatura recebida: {temperatura}°C")
    if temperatura >= LIMITE:
        print("[Detector] ⚠️ Incêndio detectado! Enviando alerta...")
        canal_alerta.basic_publish(exchange='', routing_key='alarme_incendio', body='ALERTA: Incêndio detectado')
        canal_alerta.basic_publish(exchange='', routing_key='ativar_prevencao', body='ATIVAR SISTEMA DE PREVENÇÃO')


conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexao.channel()
canal.queue_declare(queue='temperatura_cpu')

canal_alerta = conexao.channel()
canal_alerta.queue_declare(queue='alarme_incendio')
canal_alerta.queue_declare(queue='ativar_prevencao')

canal.basic_consume(queue='temperatura_cpu', on_message_callback=callback, auto_ack=True)

print('[Detector] Aguardando dados de temperatura...')
canal.start_consuming()
