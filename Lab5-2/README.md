## Estudiante: Juan Camilo Iguaran, jciguaranf@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 5-2-HDFS
# 1. Breve descripción de la actividad
GESTIÓN DE ARCHIVOS EN HDFS Y S3 PARA BIG DATA

__Conexion al cluster:__ Nos conectamos al cluster desde Putty
![Captura11](https://user-images.githubusercontent.com/46933022/199150305-de472656-718b-4c02-8454-cebd4fece89c.PNG)

__listamos los archivos:__
!![imagen](https://user-images.githubusercontent.com/46933022/199150650-f827a755-fe6f-4708-947c-178e4d9547f8.png)

__Creamos el datasets con los archivos:__
![Captura12](https://user-images.githubusercontent.com/46933022/199150799-74cf25c5-58d5-4618-b40e-0f20684c9fb2.PNG)

__Copia archivo gutenberg en servidor local (amazon s3):__
![Captura14](https://user-images.githubusercontent.com/46933022/199151123-8a5b3d36-b420-4ab5-a919-b1316237b6df.PNG)


__ls a gutenberg-small:__
![Captura13](https://user-images.githubusercontent.com/46933022/199151321-0485d115-5969-4135-9bea-a7abc6c91f74.PNG)


# Uso de otros comandos:

```
hdfs dfs -du: ver uso de disco en bytes
hdfs dfs -rm datasets/onu/hdi-data.csv: eliminar archivos
```
![Captura15](https://user-images.githubusercontent.com/46933022/199151490-d39d0235-59f9-417f-9ba8-ce751ef983d2.PNG)

```
hdfs dfs -cat datasets/otros/dataempleados.txt: mostrar contenido de archivo
```
![Captura16](https://user-images.githubusercontent.com/46933022/199152101-40b85a16-6237-4492-ac93-6150da359ab1.PNG)


# Gestion de archivos VIA HUE en amazon EMR
![Captura2](https://user-images.githubusercontent.com/46933022/199152307-0935e8be-5315-402a-ac7d-d8a892e5d5e1.PNG)

![imagen](https://user-images.githubusercontent.com/46933022/199152396-489b528a-5752-4661-a490-da415fa78c11.png)


![imagen](https://user-images.githubusercontent.com/46933022/199152495-e8ca715c-5fc0-45c7-9738-8aa1e72194f2.png)


![imagen](https://user-images.githubusercontent.com/46933022/199152624-91753c49-e43c-4ac4-af6b-22b0b3cc327f.png)


