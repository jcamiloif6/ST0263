# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Juan Camilo Iguarán Fernandez - correo institucional: jciguaranf@eafit.edu.co
Rafael Gomez - correo institucional: rgomeze@eafit.edu.co
Juan Felipe Martínez: jmartineb@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera - [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Desplegar una aplicación monolítica moodle en DCA, que cuente con un LoadBalancer en la capa de aplicación, además de implementar una base de datos y un FileSystem distribuido usando docker e implementando un certificado ssl basado en nginx

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Se configuraron los moodle 
- Se configuró la base de datos

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
- No se pudo comprobar la correcta configuración de los NFS ni en el servidor NFS ni en los Moodles ya que las reglas de firewall fueron cambiadas y no tenemos acceso ssh

![imagen](https://user-images.githubusercontent.com/46933022/200088591-240b5d4f-4be2-4fd1-b737-089855110637.png)

- No se llego a la fase final que era desplegar los moodle para ver su resultado

# 2. información general de diseño
Se utilizaron contenedores Docker para la instalación de Moodle, BD y Nginx. Cada una de las instancias tiene su propia dirección IP elástica.

# 3. Descripción del ambiente de desarrollo y técnico:

## Dirección IP y nombre de dominio
- IP elástica del balanceador: 192.168.10.163
- Dominio con certificado SSL: https://proyecto21.dis.eafit.edu.co

## Detalles técnicos
- DCA Eafit: servicio para desplegar las instancias.
- Docker: contenedor para desplegar Moodle, BD y Nginx.
- Nginx: servidor web.
- Certbot y Let's Encrypt: servicio para asignar certificado SSL.

## Descripción y cómo se configura los parámetros del proyecto 



### 6. Configuración de Docker


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
    server 192.168.10.190:80 weight=5;
    server 192.168.10.227:80 weight=5;
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

![imagen](https://user-images.githubusercontent.com/46933022/200087671-8e92f917-f3c1-48b1-9c4a-915974a47b8a.png)

Ingresar al archivo docker-compose.yml, borrar su contenido y reemplazarlo con lo siguiente:
```
version: '3.1'
services:
  nginx:
    container_name: nginx
    image: nginx
    volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
    ports:
    - 80:80
```

![imagen](https://user-images.githubusercontent.com/46933022/200087888-f6576133-9a84-4bcf-989a-f74792965fd7.png)


Inicializar Docker:
```
docker-compose up --build -d
```

![imagen](https://user-images.githubusercontent.com/46933022/200088256-543eaefa-f98d-4579-99de-abb2df2a8e36.png)
![imagen](https://user-images.githubusercontent.com/46933022/200088316-cc6de196-2376-4471-ac95-15554786c4e1.png)


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
/mnt/nfs_share 192.168.0.0/24(rw,sync,no_subtree_check,no_root_squash)
```

Actualizar las reglas de firewall para permintir el protocolo NFS:
```
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
sudo ufw allow from 172.31.0.0/24 to any port nfs
sudo ufw allow 22
sudo ufw enable
sudo ufw status
```

Nota: el comando sudo ufw allows 22 no se utilizó, pero es necesario

### 2. Instalar NFS en las instancias de wordpress(moodle1 y moodle2):
Instalar nginx en las dos instancias que tendran el moodle:
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
192.168.10.223:/mnt/nfs_share /var/www/html nfs auto 0 0
```

Crear directorio donde se compartiran los archivos (en ambas instancias):
```
sudo mkdir -p /mnt/nfs_clientshare
```

Hacer la conexion con el servidor NFS (en ambas instancias):
```
sudo mount 192.168.10.223:/mnt/nfs_share /mnt/nfs_clientshare
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

![Captura1](https://user-images.githubusercontent.com/46933022/200086800-d42371ec-649c-40d9-b4fd-91ab6af7272c.PNG)


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

![imagen](https://user-images.githubusercontent.com/46933022/200086897-f5ad0689-fbcc-4b65-9427-8dfbc6caf0aa.png)


Correr el contenedor de moodle:
```
sudo docker-compose up --build -d
```

## Finalmente
Ingresar a su dominio https://proyecto21.dis.eafit.edu.co/

![imagen](https://user-images.githubusercontent.com/46933022/200088505-0c0cdcc8-feb3-46ea-9164-7af54e573a26.png)






# 4. Referencias:
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- hhttps://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/
- https://github.com/sceballosp/Laboratorios-Telematica/tree/main/Lab4
- https://github.com/jcamiloif6/ST0263/tree/main/Lab4
