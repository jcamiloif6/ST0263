## Estudiante: Samuel Meneses Diaz, smenesesd@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 5-2-HDFS
# 1. Breve descripción de la actividad
En este laboratorio se afianzaron y se pusieron a prueba  los conocimientos en la gestion de archivos en HDFS y S3 para big data. 

__Conexion al cluster:__
![1](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/1.png)   
Nos conectamos al cluster para empezar con este lab 5-2

__listar archivos:__
![2](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/2.png)   
HDFS dfs es solo para hacer la lista de archivos HDFS

__Creacion de datasets:__
![3](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/3%20creacion_datasets.png)   
Se hace la creacion de la carpeta de datasets dentro del user hadoop

__Copia archivos locales hacia HDFS:__
![4](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/4.png)   
Se hace la copia de los archivos compilados por medio de SSH/SCP al servidor gateway por la VPN 

``` hdfs dfs -put /datasets/gutenberg/gutenberg-small.zip /user//datasets/ ```

__Verificacion de la copia de los archivos locales en el hadoop:__
![5](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/5.png)

__Archivos en Amazon s3:__
![6](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/6.png)   
```hadoop distcp``` Es una herramienta para copiar datos del inter-cluster.

__ls al gutenberg-small:__
![7](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/7.png)

__Copiar archivos de HDFS hacia el servidor(gateway):__
![8](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/8.png)

__Otros comandos para traer archivos:__
![9](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/9.png)

__Otros comandos:__
![10](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/10.png)   
DU: uso de disco en bytes

![11](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/11.png)   
MV: mover archivos

![12](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/12.png)   
CP: Copiar archivos

![13](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/13.png)
RM: Borrar archivos

![14](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/14.png)   
CAT: Mostrar contenido del archivo

![15](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/15.png)   
CHMOD: Cambiar los permisos del archivo

![16](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/16.png)   
CHOWN: Cambiar el dueño del archivo

![17](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/17.png)
CHGRP: Cambiar el grupo del archivo

__Gestion de archivos VIA HUE en amazon EMR:__
![18](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/18.png)

![19](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/19.png)

![20](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/20.png)

![21](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/21.png)

![22](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/22.png)

![23](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/23.png)

![24](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-2/img/24.png)