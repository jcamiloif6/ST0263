# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Camilo Iguarán Fernandez - correo institucional: jciguaranf@eafit.edu.co
Rafael Gomez - correo institucional: rgomeze@eafit.edu.co
Juan Felipe Martínez: jmartineb@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera - [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Desplegar una aplicación monolítica moodle, que cuente con un LoadBalancer en la capa de aplicación, además de implementar una base de datos y un FileSystem distribuido usando docker e implementando un certificado ssl basado en nginx

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Desplegar cinco instancias en AWS (loadbalancer, Moodle 1 y 2, NFS y Base de datos MySQL).
- Asignar un dominio a la dirección ip del balanceador.
- Se creó una instancia con un sistema de archivos
- Se conectó la base de datos de la instancia con las instancias de moodle
- Conseguir un certificado SSL para el dominio.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor

# 2. información general de diseño
Se utilizaron contenedores Docker para la instalación de Moodle, BD y Nginx. Cada una de las instancias tiene su propia dirección IP elástica. Las máquinas virtuales que se desplegaron fueron e2-micro

# 3. Descripción del ambiente de desarrollo y técnico:

## Dirección IP y nombre de dominio
- IP elástica del balanceador: 52.45.70.222
- Dominio con certificado SSL: https://p2.proyecto2.tk

## Detalles técnicos
- AWS EC2: servicio para desplegar las instancias.
- Docker: contenedor para desplegar Moodle, BD y Nginx.
- Nginx: servidor web.
- Certbot y Let's Encrypt: servicio para asignar certificado SSL.

## Descripción y cómo se configura los parámetros del proyecto 
### Crear cinco máquinas virtuales en AWS:
- Acceder a EC2 de AWS.
- Dar click en Lanzar Instancia.
- Configurar la instancia y habilitar HTTP y HTTPS y SSH.
- Dar click en Crear Instancia.
- Luego se reserva una dirección IP elástica distinta para cada una de las 5 instancias.

![Captura1](https://user-images.githubusercontent.com/46933022/199866521-e9b34baf-0f67-4219-b7a2-be1ceb49c30a.PNG)

![Captura2](https://user-images.githubusercontent.com/46933022/199866406-a5de3768-458b-42de-a133-1571558226d6.PNG)


### Configuración de DNS en AWS:
- En la barra de búsqueda teclear Route 53.
- Dar click en Crear Zona Alojada.
- Click en Crear Registros
- Agregar los registros A y CNAME para el dominio.
-
![Captura3](https://user-images.githubusercontent.com/46933022/199866825-f3ab8820-5f57-49b8-82d8-4314b4df72e5.PNG)



### Configurar los nameservers en el proveedor del dominio (para este laboratorio se utilizó Freenom):
- Dar click en Manage domain
- Dar click en Management tools y luego en Nameservers
- Agregar los dominios NS que da AWS a tu dominio que hayas creado en freenom o el proveedor de DNS que hayas escogido.

![Captura4](https://user-images.githubusercontent.com/46933022/199867000-eb63f130-f86a-43c6-aa09-f77c1702558c.PNG)



## Configuración de la instancia del Balanceador(load balancer):
### 1. Conectarse a la instancia por SSH:
 

### 2. Instalar certbot, let's encrypt y nginx:
Usar los siguientes comandos:
```
sudo apt update
sudo apt install python3-pip
sudo -H pip3 install certbot
sudo apt install letsencrypt -y
sudo apt install nginx -y
```
### 3. Configurar nginx.conf

Entrar al archivo de configuración:
```
sudo vim /etc/nginx/nginx.conf
```

Borrar el contenido del archivo y reemplazarlo con lo siguiente:
```
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

events {
    worker_connections  1024;  ## Default: 1024
}
http {
    server {
        listen  80 default_server;
        server_name _;
        location ~ /\.well-known/acme-challenge/ {
            allow all;
            root /var/www/letsencrypt;
            try_files $uri = 404;
            break;
        }
    }
}

```

Guardar la configuración de nginx:
```
sudo mkdir -p /var/www/letsencrypt
sudo nginx -t
sudo service nginx reload
```

### 4. Pedir los certificados ssl
Ejecutar el siguiente comando para certificados específicos (cambiar datos de correo y dominio de los siguiente comando):
```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m jciguaranf@eafit.edu.co --agree-tos -d p2.proyecto2.tk
```
Ejecutar el siguiente comando para wildcards:
```
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.proyecto2.tk--manual --preferred-challenges dns-01 certonly
```
Al ejecutar el comando anterior hay un periodo de espera en el que se debe agregar un registro TXT en el DNS para que funcione. En este periodo de tiempo debe agregar el registro TXT en la zona creada en GCP con los datos que se le dan al ejecutar el comando(nombre de DNS y clave).
![Captura10](https://user-images.githubusercontent.com/46933022/199867315-702b0ef7-42d4-4cff-adc6-71bbf2cbfc42.PNG)


### 5. Configuración de archivos:
Crear carpeta para los certificados:
```
mkdir -p nginx/ssl
```

Copiar los certificados a la carpeta creada anteriormente:
```
sudo su
cp /etc/letsencrypt/live/p2.proyecto2.tk/* /home/ubuntu/nginx/ssl/
cp /etc/letsencrypt/live/proyecto2.tk/* /home/ubuntu/nginx/ssl/
```

Crear el archivo de configuración options-ssl-nginx.conf:
```
sudo nano /etc/letsencrypt/options-ssl-nginx.conf
```

En el archivo creado anteriormente copiar lo siguiente:
```
# This file contains important security parameters. If you modify this file
# manually, Certbot will be unable to automatically provide future security
# updates. Instead, Certbot will print and log an error message with a path to
# the up-to-date file that you will need to refer to when manually updating
# this file.
ssl_session_cache shared:le_nginx_SSL:10m;
ssl_session_timeout 1440m;
ssl_session_tickets off;
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;
ssl_ciphers "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384";
```

Copiar el archivo options-ssl-nginx.conf:
```
cp /etc/letsencrypt/options-ssl-nginx.conf /home/ubuntu/nginx/ssl/
```

Acceder al directorio nginx/ssl y crear la llave ss-dhparams.pem:
```
cd nginx/ssl
openssl dhparam -out ssl-dhparams.pem 512
```

Correr los siguientes comandos:
```
DOMAIN='p2.proyecto2.tk' bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/letsencrypt/$DOMAIN.pem'
cp /etc/letsencrypt/live/lab4.ml/* /home/jciguaranf/nginx/ssl/
exit
```

### 6. Configuración de Docker
Instalar docker, docker-compose y git:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y
```

Inicializar Docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
sudo reboot
```

Clonar repositorio con la configuración de Docker y copiar archivos:
```
git clone https://github.com/st0263eafit/st0263-2022-2.git
cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp docker-compose.yml /home/ubuntu/nginx
sudo cp nginx.conf /home/ubuntu/nginx
sudo cp ssl.conf /home/ubuntu/nginx
```

Detener nginx:
```
ps ax | grep nginx
netstat -an | grep 80
sudo systemctl disable nginx
sudo systemctl stop nginx
```

Ingresar y borrar el contenido del archivo de configuracion nginx.conf(el nuevo nginx.conf, no tocar el que se creo en el paso 3) y reemplazarlo con lo siguiente:
(asegurese de cambiar las direcciones IP privadas de sus instancias con wordpress)
```
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;
events {
  worker_connections  1024;  ## Default: 1024
}
http {
  upstream loadbalancer{
    server 172.31.80.12:80 weight=5;
    server 172.31.92.93:80 weight=5;
  }
  server {
    listen 80;
    listen [::]:80;
    server_name _;
    rewrite ^ https://$host$request_uri permanent;
  }
  server {
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;
    server_name _;
    # enable subfolder method reverse proxy confs
    #include /config/nginx/proxy-confs/*.subfolder.conf;
    # all ssl related config moved to ssl.conf
    include /etc/nginx/ssl.conf;
    client_max_body_size 0;
    location / {
      proxy_pass http://loadbalancer;
      proxy_redirect off;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Server $host;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
  }
}
```

Ingresar al archivo docker-compose.yml, borrar su contenido y reemplazarlo con lo siguiente:
```
version: '3.1'
services:
  nginx:
    container_name: nginx
    image: nginx
    volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
    - ./ssl:/etc/nginx/ssl
    - ./ssl.conf:/etc/nginx/ssl.conf
    ports:
    - 80:80
    - 443:443
```

Inicializar Docker:
```
docker-compose up --build -d
```

## Configuración de la instancia del servidor NFS:
### 1. Instalar el NFS server:
Instalar el servidor NFS en la instancia del servidor:
```
sudo apt update
sudo apt install nfs-kernel-server
```

Crear carpeta para compartir archivos en el servidor NFS:
```
sudo mkdir -p /mnt/nfs_share
sudo chown -R nobody:nogroup /mnt/nfs_share/
sudo chmod 777 /mnt/nfs_share/
```

Acceder al archivo ***exports***:
```
sudo nano /etc/exports
```

Agregar la siguiente linea de código al archivo anterior
(Asegurarse de poner la subred donde se encuentran ambas maquinas moodle1 y moodle2.
Asegurarse también de no poner la línea de código comentada):
```
/mnt/nfs_share 172.31.0.0/24(rw,sync,no_subtree_check, no_root_squash)
```

Actualizar las reglas de firewall para permintir el protocolo NFS:
```
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
sudo ufw allow from 172.31.0.0/24 to any port nfs
sudo ufw enable
sudo ufw status
```

### 2. Instalar NFS en las instancias de wordpress(moodle1 y moodle2):
Instalar nginx en las dos instancias que tendran el wordpress:
```
sudo apt update
sudo apt install nginx -y
```

Instalar NFS en cada instancia:
```
sudo apt install nfs-common -y
```

Acceder al archivo fstab dentro del directorio /etc/fstab en cada instancia de moodle y agregar la siguiente linea:
(asegurarse de usar la direccion IP privada del servidor NFS)
```
172.31.31.17:/mnt/nfs_share /var/www/html nfs auto 0 0
```

Crear directorio donde se compartiran los archivos (en ambas instancias):
```
sudo mkdir -p /mnt/nfs_clientshare
```

Hacer la conexion con el servidor NFS (en ambas instancias):
```
sudo mount 172.31.31.17:/mnt/nfs_share /mnt/nfs_clientshare
```


## Comandos para la configuración de la instancia de la Base de datos:
Instalar docker y docker-compose:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y
```

Crear un directorio para el contenedor de Docker:
```
mkdir Docker
```

Acceder al directorio creado anteriormente y crear los siguientes archivos:

- ### Dockerfile
Ingresar el siguiente comando para crear y acceder al Dockerfile
```
vi Dockerfile
```

Escribir el siguiente contenido:
```
FROM mysql:8.0
```

- ### docker-compose.yaml 
Ingresar el siguiente comando para crear y acceder al docker-compose.yaml
```
vi docker-compose.yaml
```

Escribir el siguiente contenido:
```
version: '2'
services:
  mariadb:
    image: docker.io/bitnami/mariadb:10.6
    environment:
      # ALLOW_EMPTY_PASSWORD is recommended only for development.
      - ALLOW_EMPTY_PASSWORD=yes
      - MARIADB_USER=bn_moodle
      - MARIADB_DATABASE=bitnami_moodle
      - MARIADB_CHARACTER_SET=utf8mb4
      - MARIADB_COLLATE=utf8mb4_unicode_ci
    volumes:
      - 'mariadb_data:/bitnami/mariadb'
volumes:
  mariadb_data:
```

Inicializar Docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
```

Correr el contenedor con docker:
```
sudo docker-compose up --build -d
```

## Configuración de los moodle:

Repetir los siguientes pasos para cada instancia (moodle1 y moodle2)

Instalar docker y docker-compose:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y

sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
```

Detener los servicios de nginx:
```
sudo systemctl disable nginx
sudo systemctl stop nginx
```

Crear un directorio para el contenedor de Docker:
```
mkdir Docker
```

Acceder al directorio creado anteriormente y crear el siguiente archivo:

- docker-compose.yaml con el siguiente contenido:
```
version: '2'
services:
  moodle:
    image: docker.io/bitnami/moodle:4
    ports:
      - '80:8080'
      - '443:8443'
    environment:
      - MOODLE_DATABASE_HOST=mariadb
      - MOODLE_DATABASE_PORT_NUMBER=3306
      - MOODLE_DATABASE_USER=bn_moodle
      - MOODLE_DATABASE_NAME=bitnami_moodle
      # ALLOW_EMPTY_PASSWORD is recommended only for development.
      - ALLOW_EMPTY_PASSWORD=yes
    volumes:
      - 'moodle_data:/bitnami/moodle'
      - 'moodledata_data:/bitnami/moodledata'
volumes:
  moodle_data:
    driver: local
  moodledata_data:
    driver: local
```

Correr el contenedor de moodle:
```
sudo docker-compose up --build -d
```

## Finalmente
Ingresar a su dominio https://p2.proyecto2.tk

![Captura8](https://user-images.githubusercontent.com/46933022/199868890-80eafa9a-cc92-4562-96c6-267f4a93eba9.PNG)

![Captura9](https://user-images.githubusercontent.com/46933022/199868933-41db3eb5-5e2a-46cb-a443-b3368d50a548.PNG)






# 4. Referencias:
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- hhttps://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/
- https://github.com/sceballosp/Laboratorios-Telematica/tree/main/Lab4
- https://github.com/jcamiloif6/ST0263/tree/main/Lab4
