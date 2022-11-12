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

  - El grupo de seguridad del balannceador se le habilitarán las reglas de entrada http y https
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201482388-b91b9d4e-7623-4ae3-9fb4-689189b1fa6a.png)

  - El grupo de seguridad del moodle se le habilitarán las reglas de entrada http y ssh
  
  ![Captura2](https://user-images.githubusercontent.com/46933022/201482487-7d28c766-d3af-4885-90f1-268ba5ad9fc5.PNG)
  
  - El grupo de seguridad de la base de datos se le habilitarán la regla de entrada de mysql
  
  ![Captura3](https://user-images.githubusercontent.com/46933022/201482558-5083a976-c634-43a9-850b-e0673536d6fc.PNG)

  - El grupo de seguridad del efs se le habilitarán la regla de entrada de nfs
  
  ![Captura1](https://user-images.githubusercontent.com/46933022/201482611-ece1e009-02c4-42e9-95b6-e764b420db53.PNG)
  
  
 __Paso 2__. Crear el EFS y agregarle el grupo de seguridad del nfs creado anteriormente
 - En la barra de búsqueda escribir EFS
 - Click en crear sistemas de archivos
 - Name: EFS
 - VPC: Default
 - Clase de almacenamiento: Estandar
 - Click en Create
 
 ![imagen](https://user-images.githubusercontent.com/46933022/201483385-9d7036ea-e2cd-4326-ae82-7d261f19c749.png)
 
 - Entrar al EFS creado
 - Click en Red
 - Click en Administrar
 - Agregar el security group del efs creado anteriormente a cada una de las subredes
 
 ![imagen](https://user-images.githubusercontent.com/46933022/201483466-e862e50b-ab8b-4ece-bb17-3b4da26358ec.png)



__Paso 3__. Crear el RDS y agregarle el grupo de seguridad rds creado anteriormente
- En la barra de búsqueda escribir RDS
- Click en bases de datos
- Click en Crear Bases de Datos
- Método de creación de base de datos: Creación Estándar
- Motor: MariaDB
- Plantilla: Gratuita
- Sesión de Configuración
  - Identificador de BD: moodlerds
  - Nombre de Usuario Maestro: moodleuser
  - Contraseña Maestra: moodlepassword
  - Confirmar Contraseña: moodlepassword
- Sesión de Configuración de la Instancia
  - Clase de instancia de base de datos: Clases con ráfagas (incluye clases t)
  - db.t2.micro
- Sesión de Almacenamiento: 
  - Tipo de almacenamiento: SSD de uso general (gp2)
  - Almacenamiento asignado: 20
  - Escalado automático de almacenamiento: No marcar
- Sesión de Conectividad:
  - Recurso informático: Marcar No se conecte a un recurso informático EC2
  - VPC: Default
  - Grupo de subred de DB: Default
  - Grupo de seguridad de VPC (firewall): Marcar Elegir existente
  - Seleccionar el grupo de seguridad de la Base de Datos creado anteriormente
- Autenticación de bases de datos: Marcar Autenticación con Contraseña
- Click en Crear Base de datos

Esperar aproximadamente 10 minutos a que la base de datos quede creada. Así debe quedar una vez este creada:

![Captura6](https://user-images.githubusercontent.com/46933022/201484544-ca86ecfe-1b0a-4193-9e5f-3d8879887418.PNG)


__Paso 4__. Crear la instancia de moodle
- En la barra de búsqueda escribir EC2
- Click en Instancias
- Click en Crear Instancia
- Nombre: moodle-template
- Imágenes de aplicaciones y sistemas operativos (Amazon Machine Image): Ubuntu
- Tipo de Instancia: t2.micro
- Par de Claves: vockey
- Sesión configuración de Red
  - VPC: Default
  - Subred: Escoger la 1a
  - Firewall (grupos de seguridad): Marcar seleccionar grupo de seguridad existente
  - Seleccionar el grupo de seguridad del moodle creado anteriormente
  
  ![Captura8](https://user-images.githubusercontent.com/46933022/201485216-e388b246-8f48-46ff-9d60-08f281771d26.PNG)

- Sesión Configuración de almacenamiento:
  - Click en avanzado
  - En la parte donde dice Sistemas de archivos dar click en Mostrar detalles
  - Marcar EFS
  - Click en Agregar Sistemas de Archivos
  - Punto de Montaje: Cambiar /mnt/efs/fs1 por /mnt/moodle
  - 
![Captura7](https://user-images.githubusercontent.com/46933022/201485677-77fff83b-91cd-45e6-b617-1d88e31eb897.PNG)

- Click en Lanzar Instancia
