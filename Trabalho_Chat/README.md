# Este repositório contém implementações de diferentes conceitos de Sistemas Distribuídos em Python.

## Questão 1: Comunicação Cliente-Servidor Básica

Implementação de uma comunicação básica entre cliente e servidor usando sockets TCP/IP em Python.

### Arquivos:

- [cliente.py](http://cliente.py) - Implementação do cliente
- [servidor.py](http://servidor.py) - Implementação do servidor

### Como executar:

1. Primeiro, execute o servidor:

```bash
python servidor.py
```

1. Em seguida, execute o cliente:

```bash
python cliente.py
```

## Questão 2: Comunicação Criptografada

Implementação de uma comunicação segura entre cliente e servidor usando a biblioteca cryptography para criptografia.

### Requisitos adicionais:

```bash
pip install cryptography
```

### Arquivos:

- cliente_criptografado.py - Cliente com suporte à criptografia
- servidor_criptografado.py - Servidor com suporte à criptografia

## Questão 3: Chat Criptografado Multi-cliente

Implementação de um chat que permite múltiplas conexões simultâneas com mensagens criptografadas.

### Funcionalidades:

- Suporte a múltiplos clientes simultâneos
- Criptografia ponta a ponta das mensagens
- Broadcast de mensagens para todos os clientes conectados
- Sistema de threads para gerenciar múltiplas conexões

### Como executar o chat:

1. Execute o programa e escolha o modo (servidor ou cliente):

```bash
python chat_criptografado.py
```

1. Digite 's' para servidor ou 'c' para cliente quando solicitado

## Requisitos do Sistema

- Python 3.x
- Biblioteca cryptography

## Feito utilizando WSL
