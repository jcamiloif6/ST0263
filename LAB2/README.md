#
# Profesor: Edwin Nelson Montya, emontoya@eafit.edu.co

# EL OBJETIVO DE ESTA DOCUMENTACÍON ES BRINDAR UNA GUÍA Y ENTENIDMIENTO PARA PODER EJECUTAR EL LANORATORIO 1 DE LA MATERIA TÓPICOS EN TELÉMATICA

# Laboratorio1: Web Server minimalista utilizando Python Sockets montado en una máquina virtual de AWS.
#
# 1. breve descripción de la actividad
#

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se desarrolló un mini webserver utilizando python sockets, en el cual el usuario utlizando el método de Get Request realiza una petición de algún archivo que se encuentre en el programa (en este caso pdf o  jpg). A su vez, se decodifica el método en consola permitiendo ver información relevante de la petición. Si el archivo solicitado no se encuentra, el programa redirige al usuario a una página por defecto con extensión html. Adicionalmente, se despliega el servidor en una máquina virtual en AWS utilizando una ip elástica

# 2. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
## 2.1 Prerequisitos de software
1. Descargar WinSCP: https://winscp.net/eng/download.php

WinSCP (Windows Secure Copy) es un protocolo de transferencia de archivos SSH (SFTP), un protocolo de transferencia de archivos (FTP), WebDAV, Amazon S3 y un cliente de protocolo de copia segura (SCP) gratuito y de código abierto para Microsoft Windows. Su función principal es la transferencia segura de archivos entre una computadora local y un servidor remoto. En nuestro ejemplo lo utilizaremos para lograr conectar el programa que se encuentra en nuestra computadora, al servidor.

2. Descargar PuTTY: https://www.putty.org/

PuTTY será la terminal que vamos a utilizar

3. Es requisito tener la instancia de aws encendida para poder probar el programa
![Captura2Lab1](https://user-images.githubusercontent.com/46933022/183263351-088a977d-3360-4b1d-80a3-4152c4a9d6fe.PNG)

4. IP o nombres de dominio en nube o en la máquina servidor:
35.171.92.201

## 2.2 Probando programa
Es necesario iniciar sesión de Ubuntu con la Ip del servidor
![imagen](https://user-images.githubusercontent.com/46933022/183263466-9444d259-dc35-40f9-9e4b-ca22638bbc7a.png)

Una vez pegando los archivos del programa en la nueva sesión de Ubuntu de WinSCP, abrir la terminal de PuTTY y seguir los siguientes comandos de instalación de librerías y ejecución del programa:

1. sudo apt update
2. sudo apt install sodtware-properties-common
3. sudo add-apt-repository ppa:deadsnakes/ppa
4. sudo apt install python3.9
5. sudo apt-get install python3-pip
6. sudo pip3 install flask
7. screen -R <nombre>
8. screen -x <nombre>
9. sudo python3 server.py
  
# 3. Resultados
  ![Captura1Lab1](https://user-images.githubusercontent.com/46933022/183264270-c210bd13-9dba-4363-afa8-e31dbe615457.PNG)
  ![Captura3Lab1](https://user-images.githubusercontent.com/46933022/183264291-0b9a046b-439f-44ea-9065-646e9e7d9490.PNG)
  ![Captura4Lab1](https://user-images.githubusercontent.com/46933022/183264299-9f41b21b-40ba-4a19-af81-3c4c7a70b7f0.PNG)
  ![Captura5Lab1](https://user-images.githubusercontent.com/46933022/183264363-2395e1e6-6838-46f1-90bb-bfc970748528.PNG)
  ![Captura6Lab1](https://user-images.githubusercontent.com/46933022/183264321-d3f54389-500c-48c9-83ad-44c737250f2f.PNG)

# 4. Referencias
  https://www.youtube.com/watch?v=TTE-ZxN3XkA
  
#### versión README.md -> 1.0 (2022-agosto)
