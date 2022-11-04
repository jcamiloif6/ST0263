# Información de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Samuel Ceballos Posada, sceballosp@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, [emontoya@eafit.edu.co](mailto:emontoya@eafit.edu.co)

# 1. Breve descripción de la actividad
Desarrollar habilidades en el proceso de creación, despliegue y gestión de aplicaciones utilizando docker y aprender a asignar un certificado ssl válido a un dominio en Let's Encrypt.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Desplegar una instancia con un servidor wordpress en GCP.
- Asignar un dominio a la dirección ip del servidor.
- Conseguir un certificado SSL válido para el dominio.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.

# 2. información general de diseño
Se utilizaron contenedores Docker para la instalación de Wordpress en la instancia de GCP.

# 3. Descripción del ambiente de desarrollo y técnico:

## Dirección IP y nombre de dominio
- IP elástica: 34.171.159.72
- Dominio: sceballosp.tk
- Dominio con certificacion: https://www.sceballosp.tk

## Detalles técnicos
- GCP: servicio para desplegar la instancia.
- Docker: contenedor para desplegar wordpress.
- Nginx: servidor web.
- Certbot y Let's Encrypt: servicio para asignar certificado SSL.

## Descripción y cómo se configura los parámetros del proyecto 
### Crear una máquina virtual en GCP:
- Acceder a la consola de GCP (console.cloud.google.com).
- Dar click en **Compute Engine**.
- Dar click en **Crear Instancia**.
- Configurar la instancia para que sea de tipo ec2-micro y habilitar HTTP y HTTPS.
- Dar click en **CREAR**.

![Instancia](https://user-images.githubusercontent.com/60147093/190934959-6b297ddb-728c-46ac-b361-44951154cb60.PNG)

### Asignar IP elastica a la instancia creada:
- Dar click en el menú de navegación.
- Dar click en **Red de VPC**.
- Dar click en **Direcciones IP**.
- Seleccionar la IP externa de la instancia creada y dar click en **RESERVAR**.

![Ip elastica](https://user-images.githubusercontent.com/60147093/190934974-5ceba6b8-581e-44dd-8830-4cec918b6ffe.PNG)

### Configurar DNS en GCP:
- En la barra de búsqueda ingresar *Cloud DNS*.
- Dar click en **Crear Zona**.
- Agregar los registros **A** y **CNAME** para el dominio.

![DNS](https://user-images.githubusercontent.com/60147093/190934986-ed8eb1a7-a60c-4664-866c-3d42f2e009ca.PNG)

### Configurar los nameservers en el proveedor del dominio (Freenom):
- Dar click en **Manage domain**
- Dar click en **Management tools** -> **Nameservers**
- Agregar los dominios NS que da GCP.

![Freenom](https://user-images.githubusercontent.com/60147093/190935004-0951fdce-8c41-4871-8dbc-ead82a190ff4.PNG)

## Configuración del servidor:
### Conectarse a la instancia por SSH:
- Acceder a la consola de GCP.
- Dar click en **Compute Engine**.
- Dar click en **VM Instances**.
- Dar click en el botón *SSH* de la instancia deseada. 

### Instalar certbot, let's encrypt y nginx:
Usar los siguientes comandos:
```
sudo apt update
sudo apt install python3-pip
sudo -H pip3 install certbot
sudo apt install letsencrypt -y
sudo apt install nginx -y
```
### Configurar nginx.conf

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

### Pedir los certificados ssl
Ejecutar el siguiente comando para certificados específicos (ej. www):
```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m sceballosp@eafit.edu.co --agree-tos -d www.sceballosp.tk
```
Ejecutar el siguiente comando para wildcards:
```
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.sceballosp.tk --manual --preferred-challenges dns-01 certonly
```
- **IMPORTANTE:** Al ejecutar el comando anterior hay un periodo de espera en el que se debe agregar un registro TXT en el DNS para que funcione. 

Crear carpeta para el wordpress y los certificados:
```
mkdir /home/sceballosp/wordpress
mkdir /home/sceballosp/wordpress/ssl
```

Copiar los certificados a las carpetas creadas anteriormente:
```
sudo su
cp /etc/letsencrypt/live/www.danielanino.tk/* /home/dxninob/wordpress/ssl/
cp /etc/letsencrypt/live/danielanino.tk/* /home/dxninob/wordpress/ssl/
```

### Configuración de Docker y Wordpress
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
sudo usermod -a -G docker dxninob
sudo reboot
```

Clonar repositorio con la configuración de Docker y copiar archivos:
```
git clone https://github.com/st0263eafit/st0263-2022-2.git
cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp docker-compose.yml /home/sceballosp/wordpress
sudo cp nginx.conf /home/sceballosp/wordpress
sudo cp ssl.conf /home/sceballosp/wordpress
```

Detener nginx:
```
ps ax | grep nginx
netstat -an | grep 80
sudo systemctl disable nginx
sudo systemctl stop nginx
```

Inicializar Docker con Wordpress:
```
cd /home/dxninob/wordpress
docker-compose up --build -d
```

## Resultados
Ingresar a https://www.sceballosp.tk

![Pagina](https://user-images.githubusercontent.com/60147093/190935033-fb9cb8b4-1504-44d8-8256-54a10424b013.PNG)

Se puede ver el certificado SSL:

![Certificado](https://user-images.githubusercontent.com/60147093/190935049-71df96bf-5f76-4e3d-ad2d-ab7ac1ac9a32.PNG)

# 4. Información relevante

## Referencias:
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
- https://www.letscloud.io/community/how-to-set-up-an-nginx-with-certbot-on-ubuntu
- https://geekrewind.com/setup-lets-encrypt-wildcard-on-ubuntu-20-04-18-04/
