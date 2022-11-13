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
- Dominio con balanceador de AWS:  www.proyecto2.tk
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
## Parte 1
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

![imagen](https://user-images.githubusercontent.com/46933022/201494922-5adb43b9-05c2-428c-9713-9a921a192e96.png)


- Una vez creada la instancia, entrar por ssh a ella
- Instalar docker y docker-compose
```
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y
```

- Inicializar Docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
sudo reboot
```

- Poner los siguientes comandos
```
mkdir moodle
sudo nano docker-compose.yml
```
- Pegar el siguiente contenido
```
version: '2'
services:
  moodle:
    image: docker.io/bitnami/moodle:4
    ports:
      - '80:8080'
    environment:
      - MOODLE_DATABASE_HOST=moodlereds1.c2nu2sypx880.us-east-1.rds.amazonaws.com
      - MOODLE_DATABASE_PORT_NUMBER=3306
      - MOODLE_DATABASE_USER=moodleuser
      - MOODLE_DATABASE_NAME=bitnami_moodle
      - MOODLE_DATABASE_PASSWORD=moodlepassword
      # ALLOW_EMPTY_PASSWORD is recommended only for development.
    volumes:
      - '/mnt/moodle/moodle_data:/bitnami/moodle'
      - '/mnt/moodle/moodledata_data:/bitnami/moodledata'
```      

- Probar que se conecto el EFS
``` 
mount
``` 

![Captura9](https://user-images.githubusercontent.com/46933022/201495191-7d969001-bc0a-4dff-8f0e-c7607c352692.PNG)

- Ingresar siguiente comando para borrar contenido de EFS
``` 
sudo rm -rf /mnt/moodle/*
``` 

- Probar conexión con base de datos(ingresar url que da la base de datos rds)
``` 
mysql -u moodleuser -h moodlereds1.c2nu2sypx880.us-east-1.rds.amazonaws.com -p
``` 

![Captura10](https://user-images.githubusercontent.com/46933022/201495316-c9cbd138-b8ac-49b9-bdce-a7fd6d6a476d.PNG)

- Crear base de datos
``` 
CREATE database bitnami_moodle;
``` 

![Captura11](https://user-images.githubusercontent.com/46933022/201495405-9062404e-611a-4e5b-9396-1e30f2b7a731.PNG)

``` 
cd moodle
docker-compose up
``` 

![imagen](https://user-images.githubusercontent.com/46933022/201495513-1fe82266-65ba-48a6-ad8a-49c446228f8a.png)

- Copiar y pegar ip pública en el browser. El resultado debería ser el siguiente

![imagen](https://user-images.githubusercontent.com/46933022/201495544-f2e5d708-c09d-4482-bf42-848b21ac93dc.png)


## Parte 2

### Crear una AMI para para el Servicio de Auto Scaling.
A continuación, vamos a crear una AMI del servidor web que contiene el moodle. De esta forma se guardarán el contenido del boot disk y las nuevas instancias desplegadas a partir de esta se van a instanciar con un contenido idéntico. Es así como una Amazon Machine Image se convierte en una plantilla que contiene una configuración básica la cual sirve para instanciar posteriormente máquinas.

- Para crear una AMI, en el home seleccione el servicio de EC2
- Seleccione la instancia del moodle creada anteriormente en la parte 1
- Click en Actions
- Click en Imagen y Plantillas
- Click en Crear Imagen
- Configurar los siguientes parámetros
  - Image name: Web Moodle  AMI
  - Image description: AMI for Web Server
  - Click en Create Image
  
  ![Captura14](https://user-images.githubusercontent.com/46933022/201496162-15aadb4a-086f-43d8-ab11-53f4d3a9b84f.PNG)
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201496130-998b8e5e-c62a-41a2-bfed-974d88bdec88.png)


### Crear un Target Group
Ir al menú de EC2, en la sección de Balanceadores de Carga, escoga Grupos de destino. Seleccione la opción de “Crear grupos de destino”
- Poner las siguientes configuraciones
  - Choose  a target type: Instances
  - Target group name: TG-MyWebApp
  - Protocol: HTTP:80
  - VPC: VPC-default
  - Protocol version: HTTP1
  - Click en Siguiente
  - Click en ‘create target group’
  
![Captura15](https://user-images.githubusercontent.com/46933022/201496551-bdd4b6d5-a4bd-4436-b46a-4ff4f2bd328f.PNG)

### Crear y configurar un balanceador de carga.
- En la barra de búsqueda seleccionar EC2
- En el panel izquierdo, click en Load Balancers
- Click en Create Load Balancer
- Click en Create en la sección de Application Load Balancer
- Sección de configuración básica:
  - Name: ELB-MyWebApp
  - Scheme: Seleccione internet-facing.
  - IP address type: ipv4
  - VPC: VPC-default.
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201496851-4f44fcac-8cef-4f6b-b691-b20cc7aa4c31.png)
  
  ![Captura17](https://user-images.githubusercontent.com/46933022/201496864-373d783f-1854-43b8-beef-959751aca229.PNG)


- Sección de Listeners:
  - Load Balancer Protocol: http
  - Load Balancer Port: 80.
  - Default action: seleccione el Target Group Creado: TG-MyWebApp
  - Click en add listener para crear el litener para HTTPS
    - Load Balancer Protocol: https
    - Load Balancer Port: 443
    - Click en Create Target Group y crear un grupo de seguridad, así como el creado anteriormente y asociarlo a este listener
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201497097-4d30eb48-a904-4619-9b60-e6699f9cb7a2.png)

- Sección de Network mapping:
  - VPC: VPC-default
  - Mappings: Seleccione la casilla de cada zona de disponibilidad.  Y seleccione la subred pública para ambas zonas. Recuerde que el balanceador de carga va     desplegado en la subred pública.
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201497229-3cd83b53-c4bf-4e52-8b54-0ac8e8fd4bf0.png)
  
- Sección de Security Group
  - Seleccione la opción de escoger un security group existente.
  - Escoga el grupo de seguridad web y del balanceador, creados anteriormente
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201497328-d8992db9-e84b-4709-addc-65c94fce93b0.png)
  
- Adicionarle el Listener en HTTPS con certificado SSL en Letsencrypt
  - Importar los datos con ACM
  - Certificate private key: Contenido del privkey.pem del certificado SSL que se encuentra en la carpeta ssl que se creó cuando se pidió el certificado
  - Certificate body: Contenido del cert.pem del certificado SSL que se encuentra en la carpeta ssl que se creó cuando se pidió el certificado
  - Certificate chain: Contenido del chain.pem del certificado SSL que se encuentra en la carpeta ssl que se creó cuando se pidió el certificado
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201497590-45f85d53-7877-41e0-82a7-a2ee0f1e10c3.png)

- Click en Create Load Balancer  

### Crear y configurar un Launch Template & Grupo de Auto Scaling.
#### Launch Template:
- En la barra de búsqueda selecciona EC2
- En el panel izquierdo, seleccione Launch Template, en la Sección Instancias
- Click en Create launch template
- Launch configuration name: MyWebApp
- Template version description: Template for web moodle.
- Orientación sobre Auto Scaling: Activar Casila
- Sección Contenido de la plantilla de lanzamiento:
  - Imágenes de aplicaciones y sistemas operativos (Amazon Machine Image): En Mis AMI, click en De mi Propiedad, aparecerá Web Moodle AMI
- Tipo de instancia: t2.micro
- Par de claves (inicio de sesión): Vockey
- Click en “Crear plantilla de lanzamiento”

![Captura25](https://user-images.githubusercontent.com/46933022/201531711-1de23322-fa5f-40ff-85a5-bd0fa06891ee.PNG)

![imagen](https://user-images.githubusercontent.com/46933022/201531736-64acc023-8c0d-46b7-963a-5bfb8170189b.png)

####Grupo de Autoscaling:
- Seleccione la plantilla de lanzamiento creada
- Click en el menú Actions. Click en Create auto scaling group.
- Name: MyWebApp-Auto Scaling Group
- Plantilla de lanzamiento: MyWebApp
- Click en Next
- Sección de Red
  - Network: VPC-default.
  - Subnet: Seleccione las subredes públicas ubicadas en las zonas de disponibilidad.
  - Click en Next.

![imagen](https://user-images.githubusercontent.com/46933022/201533709-a0e49a00-b840-4f47-9d26-6cccbb4fec97.png)

- Sección de Configuraciones avanzadas
  - Seleccione la casilla para: Asociar a un balanceador de carga existente.
  - Escoga: Elegir entre los grupos de destino del balanceador de cargas
  - Escoja los targets groups que se creó para la aplicación. TG-MyWebApp y TG-MyWebApps.
  - Marque la casilla: Habilitar la recopilación de métricas de grupo en CloudWatch
  - Click en Next
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201533973-5763ef09-b788-4d89-a7d4-97b87beb4078.png)
  
- Sección de Configurar políticas de escalado y tamaño de grupo
  - Caaicdad deseada: 2
  - Capacidad mínima: 2
  - Capacidad máxima: 3 
  - Políticas de escalado:
    - Seleccione Política de escalado de seguimiento de destino
    - Scaling policy name: MyWebApp-ScalingPolicy
    - Tipo de métrica: Utilización promedio de la CPU
    - Target Value: 60
    
    ![imagen](https://user-images.githubusercontent.com/46933022/201534949-5a006beb-d681-494d-b945-cd891e255531.png)

  - Click en “next”

- Click en Next. Add notifications.
- Sección Añadir Etiquetas
  - Click en “Add tag”
  - Key: Name
  - Value: WebServer
  - Click Next
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201535139-46f68884-af84-4faf-8868-bd4085ac3d89.png)

- Click en Create Auto Scaling Group.

![Captura26](https://user-images.githubusercontent.com/46933022/201535201-d6202b96-4e89-4049-a018-2744b0837641.PNG)

### Verifique el Funcionamiento del Balanceador de Carga.
- En el panel de navegación izquierdo:
  - Click en Load Balancers.
  - En el panel inferior, copie el DNS name del balanceador de carga.
  - En una nueva ventana de browser, pegue la url copiada y presione enter.
  - Usted deberá ver la página de bienvenida del servidor web de moodle.
  - Copie y pegue tambien el dominio: https://p2.proyecto2.tk y www.proyecto2.tk
  ![Captura29](https://user-images.githubusercontent.com/46933022/201535417-91d8a0b7-3975-4a97-b70a-c45cbe1dc36f.PNG)
  
  ![imagen](https://user-images.githubusercontent.com/46933022/201536850-4f2197f2-47df-46cb-a842-d7bf6d14c031.png)



# 4. Referencias
https://docs.google.com/document/d/1jtZBV9h_guHMZzr6ZLSDtEDUB04xUVDT/edit#

