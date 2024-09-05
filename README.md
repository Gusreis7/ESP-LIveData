# **ESP-LiveData** 

### **Monitoramento em tempo real de umidade e temperatura com ESP32**

Este repositório faz parte de um estudo prático em **Internet das Coisas (IoT)**, com foco na coleta e tratamento de dados de sensores usando o microcontrolador ESP32. O objetivo é criar uma aplicação que exiba dados em tempo real utilizando o sensor DHT11 e visualize as informações de maneira clara e organizada.

## **Visão Geral**

Neste projeto, utilizamos um **ESP32** e um sensor de **umidade e temperatura DHT11** para capturar dados ambientais. Esses dados são enviados para uma aplicação **Flask** que exibe gráficos em tempo real.

Em estágios futuros, o projeto será expandido com a implementação de uma arquitetura baseada em **MQTT** para a publicação e assinatura dos dados, além da integração com o **Google Cloud Platform (GCP)** para o armazenamento em um **data lake**.

---

## **Componentes**

- **ESP32**: Microcontrolador para coleta e envio de dados.
- **DHT11**: Sensor de umidade e temperatura.
- **Flask**: Framework web para criar a interface de visualização.
- **Chart.js**: Biblioteca JavaScript para a geração dos gráficos.
- **MQTT** (Futuro): Protocolo para a comunicação entre dispositivos IoT.
- **GCP** (Futuro): Infraestrutura para armazenamento dos dados em um data lake.

---
## **Codigo para o ESP32**
O codigo para o esp32 está disponivel originalmente em: 
- https://randomnerdtutorials.com/esp8266-dht11dht22-temperature-and-humidity-web-server-with-arduino-ide/
Foram realizadas pequenas mudanças esteticas apenas, disponiveis no codigo [simple_monitoring.ino](esp-scripts/)


## **Instalação e Execução**


1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/esp-livedata.git
   cd esp-livedata

2. **Crie a imagem docker**
     ```bash
    docker build -f Dockerfile_flaskapp . -t flask-sensor-app

3. **Rode o docker compose**
     ```bash
    docker compose -f docker-compose_flaskapp.yml up