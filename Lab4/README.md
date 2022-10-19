# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Camilo Iguarán Fernandez - correo institucional: jciguaranf@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera - [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Desplegar una aplicación monolítica en 2 nodos, que cuente con un LoadBalancer en la capa de aplicación, además de implementar una base de datos y un FileSystem distribuido usando docker e implementando un certificado ssl basado en nginx

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Desplegar cinco instancias en GCP (loadbalancer, Wordpress 1 y 2, NFS y Base de datos MySQL).
- Asignar un dominio a la dirección ip del balanceador.
- Se creó una instancia con un sistema de archivos
- Se conectó la base de datos de la instancia con las instancias de wordpress
- Conseguir un certificado SSL para el dominio.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor

# 2. información general de diseño
Se utilizaron contenedores Docker para la instalación de Wordpress, MySQL y Nginx. Cada una de las instancias tiene su propia dirección IP elástica. Las máquinas virtuales que se desplegaron fueron e2-small

# 3. Descripción del ambiente de desarrollo y técnico:

## Dirección IP y nombre de dominio
- IP elástica del balanceador: 34.173.255.32
- Dominio con certificado SSL: https://lab4.ml

## Detalles técnicos
- GCP: servicio para desplegar las instancias.
- Docker: contenedor para desplegar Wordpress, MySQL y Nginx.
- Nginx: servidor web.
- Certbot y Let's Encrypt: servicio para asignar certificado SSL.

## Descripción y cómo se configura los parámetros del proyecto 
### Crear cinco máquinas virtuales en GCP:
- Acceder a la consola de GCP.
- Dar click en Compute Engine.
- Dar click en Crear Instancia.
- Configurar la instancia y habilitar HTTP y HTTPS.
- Dar click en CREAR.

![imagen](https://user-images.githubusercontent.com/46933022/196772152-1847c964-cc4c-4759-a195-c523903e6a09.png)
![imagen](https://user-images.githubusercontent.com/46933022/196772250-b037b107-51cb-4e5d-83aa-20a1295c278f.png)


Luego se reserva una dirección IP elástica distinta para cada una de las 5 instancias.


### Configuración de DNS en GCP:
- Desde el menú de navegación dar click en Servicios de Red e ingresar a Cloud DNS.
- Dar click en Crear Zona.
- Agregar los registros A y CNAME para el dominio.

![imagen](https://user-images.githubusercontent.com/46933022/196773420-2d71234f-d56a-4793-aea7-d3fc1e86e259.png)


### Configurar los nameservers en el proveedor del dominio (para este laboratorio se utilizó Freenom):
- Dar click en Manage domain
- Dar click en Management tools y luego en Nameservers
- Agregar los dominios NS que da GCP a tu dominio que hayas creado en freenom o el proveedor de DNS que hayas escogido.

![imagen](https://user-images.githubusercontent.com/46933022/196773776-076169ef-2b38-478a-9f2f-4a626a7f6ac1.png)


## Configuración de la instancia del Balanceador(load balancer):
### 1. Conectarse a la instancia por SSH:

 Dar click en el botón SSH de la instancia del balanceador. 

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
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m jciguaranf@eafit.edu.co --agree-tos -d lab4.ml
```
Ejecutar el siguiente comando para wildcards:
```
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.lab4.ml--manual --preferred-challenges dns-01 certonly
```
Al ejecutar el comando anterior hay un periodo de espera en el que se debe agregar un registro TXT en el DNS para que funcione. En este periodo de tiempo debe agregar el registro TXT en la zona creada en GCP con los datos que se le dan al ejecutar el comando(nombre de DNS y clave).
![imagen](https://user-images.githubusercontent.com/46933022/196775172-bfc6055c-f43e-4515-a088-64b006bea2f1.png)


### 5. Configuración de archivos:
Crear carpeta para los certificados:
```
mkdir -p nginx/ssl
```

Copiar los certificados a la carpeta creada anteriormente:
```
sudo su
cp /etc/letsencrypt/live/lab4.ml/* /home/jciguaranf/nginx/ssl/
cp /etc/letsencrypt/live/lab4.ml/* /home/jciguaranf/nginx/ssl/
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
cp /etc/letsencrypt/options-ssl-nginx.conf /home/jciguaranf/nginx/ssl/
```

Acceder al directorio nginx/ssl y crear la llave ss-dhparams.pem:
```
cd nginx/ssl
openssl dhparam -out ssl-dhparams.pem 512
```

Correr los siguientes comandos:
```
DOMAIN='lab4.ml' bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/letsencrypt/$DOMAIN.pem'
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
sudo usermod -a -G docker jciguaranf
sudo reboot
```

Clonar repositorio con la configuración de Docker y copiar archivos:
```
git clone https://github.com/st0263eafit/st0263-2022-2.git
cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp docker-compose.yml /home/jciguaranf/nginx
sudo cp nginx.conf /home/jciguaranf/nginx
sudo cp ssl.conf /home/jciguaranf/nginx
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
    server 10.128.0.12:80 weight=5;
    server 10.128.0.13:80 weight=5;
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
(Asegurarse de poner la subred donde se encuentran ambas maquinas cms1 y cms2.
Asegurarse también de no poner la línea de código comentada):
```
/mnt/nfs_share 10.128.0.0/20(rw,sync,no_subtree_check)
```

Actualizar las reglas de firewall para permintir el protocolo NFS:
```
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
sudo ufw allow from 10.128.0.0/20 to any port nfs
sudo ufw enable
sudo ufw status
```

### 2. Instalar NFS en las instancias de wordpress(cms1 y cms2):
Instalar nginx en las dos instancias que tendran el wordpress:
```
sudo apt update
sudo apt install nginx -y
```

Instalar NFS en cada instancia:
```
sudo apt install nfs-common -y
```

Acceder al archivo fstab dentro del directorio /etc/fstab en cada instancia de wordpress y agregar la siguiente linea:
(asegurarse de usar la direccion IP privada del servidor NFS)
```
10.128.0.15:/mnt/nfs_share /var/www/html nfs auto 0 0
```

Crear directorio donde se compartiran los archivos (en ambas instancias):
```
sudo mkdir -p /mnt/nfs_clientshare
```

Hacer la conexion con el servidor NFS (en ambas instancias):
```
sudo mount 10.128.0.15:/mnt/nfs_share /mnt/nfs_clientshare
```

Verifique el funcionamiento:

- En la instancia de NFS server:
```
cd /mnt/nfs_share/
sudo touch sample1.text sample2.text
```
![nfsPrueba](https://user-images.githubusercontent.com/46933022/196778905-6d9be990-38b2-4891-bbab-4b529c13a4fb.PNG)


- En las instancias de los wordpress(cms1 y cms2):
```
ls -l /mnt/nfs_clientshare/
```
![cms1NFSPrueba](https://user-images.githubusercontent.com/46933022/196779054-d1b53fdc-871e-42d8-8215-9d26ace53c43.PNG)

![cms2NFSPrueba](https://user-images.githubusercontent.com/46933022/196779073-dd2fc6a6-4f7f-4659-a027-c25f952fb7b6.PNG)


## Comandos para la configuración de la instancia de la Base de datos MySQL:
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
version: "3.7"
services:
  mysql:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: dbserver
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: "1234"
      MYSQL_DATABASE: "wordpressdb"
    volumes:
      - ./schemas:/var/lib/mysql:rw
volumes:
  schemas: {}
```

Inicializar Docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker jciguaranf
```

Correr el contenedor con MySQL y acceder:
```
sudo docker-compose up --build -d
sudo docker exec -it dbserver mysql  -p
```
A continuación le pedirá que digite la contraseña para acceder a la base de datos. La contraseña en este ejemplo es "1234".

Crear la base de datos y los usuarios ingresando los comandos que se ven en el pantallazo:

![mysql](https://user-images.githubusercontent.com/46933022/196781297-5ff867b9-ae77-46a3-bc02-20fc5f5797f1.PNG)


## Configuración de los wordpress:

Repetir los siguientes pasos para cada instancia (cms1 y cms2)

Instalar docker y docker-compose:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y

sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker jciguaranf
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

- docker-compose.yaml con el siguiente contenido (Poner la IP privada de a instancia de la base de datos):
```
version: '3.7'
services:
  wordpress:
    container_name: wordpress
    image: wordpress:latest
    restart: always
    environment:
      WORDPRESS_DB_HOST: 10.128.0.14:3306
      WORDPRESS_DB_USER: cms1
      WORDPRESS_DB_PASSWORD: 1234
      WORDPRESS_DB_NAME: wpd
    volumes:
      - /var/www/html:/var/www/html
    ports:
      - 80:80
volumes:
  wordpress:
```

Correr el contenedor de wordpress:
```
sudo docker-compose up --build -d
```

## Finalmente
Ingresar a su dominio https://lab4.ml




# 4. Referencias:
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- hhttps://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/
- https://github.com/sceballosp/Laboratorios-Telematica/tree/main/Lab4
