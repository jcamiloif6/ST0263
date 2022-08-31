#
# Profesor: Edwin Nelson Montya, emontoya@eafit.edu.co

# EL OBJETIVO DE ESTA DOCUMENTACÍON ES BRINDAR UNA GUÍA Y ENTENIDMIENTO PARA PODER EJECUTAR EL LABORATORIO 2 DE LA MATERIA TÓPICOS EN TELÉMATICA

# Laboratorio2: Implementación Servidor RabbitMQ enviando datos de temperatura mediante un cliente a un servidor mediante RabbitMQ.
#
# 1. breve descripción de la actividad
#

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se desarrolló un cliente de manera local que envía mensajes a un servidor utilizando el broker de mensajería de RabbitMQ. Mediante el cliente el usuario envía mensajes pedidos (en este caso datos de temperatura y humedad) y con enviados a una cola que se mostrará por consola. Se crean dos colas que desempaquetarán estos mensajes. Rabbit utiliza el protocolo AMQP.

# 2. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
## 2.1 Prerequisitos de software
1. Descargar e instalar RabbitMQ: https://www.rabbitmq.com/download.html
2. Desde Visual Studio 2022 instalar extensión de RabbitMQ. Es indispensable.

## 2.2 Probando programa
1. Abrir dentro de la carpeta ConsumidorDEMO, el archivo ConsumidorDEMO.sln
2. Abrir dentro de la carpeta ProyectorMQ, el archivo ProyectorMQ.sln
3. En ConsumidorDEMO.sln compilar solución y copiar dirección que se muestra en la salida de la consola
4. Abrir dos consolas y pararse en la dirección dada al compilar ConsumidorDEMO.sln
5. En una consola ejecutar el comando: "ConsumidorDEMO.exe cola1" y en la otra "ConsumidorDEMO.exe cola2"
6. En proyectorMQ ejecutar solución
  
# 3. Resultados
  ![imagen](https://user-images.githubusercontent.com/46933022/187586745-6595ca18-2c8c-4cd1-b2be-425096c0f220.png)
  ![imagen](https://user-images.githubusercontent.com/46933022/187586910-487c24fa-847e-45eb-95a4-1a56a7bcd4e9.png)
  
 # 4. Adicionales
Se agregaron soluciones para enviar datos através de arduino, envía datos pero el consumidor no los recibe. Implementación incompleta.
  
# 5. Referencias
  https://www.youtube.com/watch?v=4Qdh6D5JH_U
  
#### versión README.md -> 1.0 (2022-agosto)
