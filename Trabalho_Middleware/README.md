## Sistema de Monitoramento de Temperatura com RabbitMQ

Este projeto implementa um sistema de monitoramento de temperatura usando RabbitMQ para comunicação entre componentes.

### Componentes do Sistema:

- **Produtor (produtor.py):** Monitora a temperatura da CPU e publica as leituras
- **Detector (detector_incendio.py):** Analisa as temperaturas e gera alertas quando necessário
- **Consumidor (alarme_prevencao.py):** Recebe e processa os alertas, ativando sistemas de alarme e prevenção

### Requisitos:

- Python 3.x
- RabbitMQ Server
- Biblioteca pika
- Biblioteca psutil

### Instalação:

```bash
pip install pika psutil
```

### Como Executar:

1. Inicie o servidor RabbitMQ
2. Execute o consumidor em um terminal:
    
    ```bash
    python alarme_prevencao.py
    ```
    
3. Execute o detector em outro terminal:
    
    ```bash
    python detector_incendio.py
    ```
    
4. Execute o produtor em um terceiro terminal:
    
    ```bash
    python produtor.py
    ```
    

### Funcionamento:

1. O produtor coleta a temperatura da CPU a cada 5 segundos e publica na fila 'temperatura_cpu'
2. O detector monitora as temperaturas e, se ultrapassar 70°C, envia alertas para as filas 'alarme_incendio' e 'ativar_prevencao'
3. O consumidor processa os alertas e aciona os sistemas de alarme e prevenção

### Observações:

- O sistema usa valores fictícios de temperatura caso não consiga ler os sensores reais
- O alarme emite um som de alerta quando ativado
