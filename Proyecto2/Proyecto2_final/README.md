# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Camilo Iguarán Fernandez - correo institucional: jciguaranf@eafit.edu.co
Rafael Gomez - correo institucional: rgomeze@eafit.edu.co
Juan Felipe Martínez: jmartineb@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera - [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Desplegar una aplicación de moodle utilizando una base de datos RDS, un file system (EFS) y un Load Balancer administrados por aws, mejorando así escalabilidad, rendimiento y disponibilidad de la aplicación

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Creación y conexión de base de datos RDS con instancia que tiene el moodle
- Creación y conexión de un File System EFS con la instancia del moodle
- Creación de un Load Balancer provisto por AWS con el certificado ssl creado anteriormente
- Despliegue de la aplicación logrando monitoreo en rendimiento, dispnibilidad y escalabilidad

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
En ocaciones la aplicación no se muestra correctamente sacando un mensaje en el navegador de 502 Gateway Time-Out

# 2. información general de diseño
Se utilizó una instancia e2.micro agregandole un EFS creado anteriormente. Se utilizó un EFS creado en AWS, se utilizó Un Load Balancer agregandole una plantilla y un Grupo de destino determinado. También se utilizó una base de datos RDS con motor de MariaDB

# 3. Descripción del ambiente de desarrollo y técnico:

## Dirección IP y nombre de dominio
- Dominio con certificado SSL: https://p2.proyecto2.tk
- ELB-MyWebApp-2023056246.us-east-1.elb.amazonaws.com

## Detalles técnicos
- AWS EC2: servicio para desplegar la instancia de Moodle.
- Docker: contenedor para desplegar Moodle
- Nginx: servidor web.
- Certbot y Let's Encrypt: servicio para asignar certificado SSL.
- RDS: Base de datos de AWS
- EFS: File System de AWS
- Load Balancer y Target Gropus: Balanceador de carga y Grupos de destino 
- Template: Plantilla de AWS para grupo de Auto Scalling

## Descripción y cómo se configura los parámetros del proyecto 
### Parte 1
__Paso 1__. Crear cuatro grupo de seguridad. uno para el Balanceador, otro para el moodle, otro para la base de datos y otro para el efs

  --__1.1__. El grupo de seguridad del balannceador se le habilitarán las reglas de entrada http y https
  
  
