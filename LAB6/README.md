## Estudiante: Juan Camilo Iguarán, jciguaranf@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 6 PYSPARK
# 

### Introducción
- Entrar al nodo master por ssh cluster
- Poner los siguientes comandos:
  ```
  sudo yum install git -y
  git clone https://github.com/st0263eafit/st0263-2022-2.git
  cd st0263-2022-2
  pyspark
  ```
  
![Captura1](https://user-images.githubusercontent.com/46933022/202078588-6909455d-2964-499a-82b4-64454600a6c1.PNG)


## Parte 1

### 1. ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.

- Datasets en Hadoop

![imagen](https://user-images.githubusercontent.com/46933022/202078889-6b449a2f-ad49-47ed-b9cc-de042353b005.png)

- Ejecutar los siguientes comandos

![Captura4](https://user-images.githubusercontent.com/46933022/202079190-c7b0288f-3fc6-455d-a30f-6344387458b5.PNG)

![Captura5](https://user-images.githubusercontent.com/46933022/202079072-7d25ac39-0706-4483-931d-5be4c99701c5.PNG)

### 2. ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.

- Datasets en S3

![Captura2](https://user-images.githubusercontent.com/46933022/202079317-c127e6d2-fb48-4c67-b09a-595242d5a996.PNG)

- Ejectuar los siguientes comandos para S3

![Captura3](https://user-images.githubusercontent.com/46933022/202079383-a3a8a6a4-e92c-4c4c-8c25-5425e0fefec3.PNG)

### 3. ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.

- Ingresar a la URL de Juypiter Notebooks en tu cluster
- Crea un notebook
- Ingresa al notebook y digita los siguientes comandos

![Captura6](https://user-images.githubusercontent.com/46933022/202079852-1b1adcb0-c18b-4365-a2cd-56e1822a76dc.PNG)

- En el nodo master por ssh verificamos la creación de los archivos siguiendo los siguientes comandos

![Captura7](https://user-images.githubusercontent.com/46933022/202079979-14072856-3889-42f9-98a2-ce11fb835049.PNG)

## Parte 2
### Replique, ejecute y ENTIENDA el notebook: Data_processing_using_PySpark.ipynb con los datos respectivos, ejecutelo en AWS EMR.

En el notebook de jupyter digitar los siguientes comandos

![Captura8](https://user-images.githubusercontent.com/46933022/202080919-ee90d162-af0b-4eb1-8a06-15c7031382e2.PNG)
![Captura9](https://user-images.githubusercontent.com/46933022/202080927-2bafd324-ee6d-4131-a4cf-17365105b28a.PNG)
![Captura10](https://user-images.githubusercontent.com/46933022/202080964-f2572aa3-6bb3-44b5-af06-ba58bb6a8ad8.PNG)
![Captura11](https://user-images.githubusercontent.com/46933022/202080969-01a97579-ae10-4b91-9fe6-534677401db0.PNG)
![Captura12](https://user-images.githubusercontent.com/46933022/202081023-798d3ac6-df22-427e-a4f7-5e7d08ac976d.PNG)
![Captura13](https://user-images.githubusercontent.com/46933022/202081034-e34f22cb-494a-4dc0-8b6c-1c54e4fb7ee4.PNG)
![Captura14](https://user-images.githubusercontent.com/46933022/202081041-6e08c7ad-2464-43af-8864-e982ce399b06.PNG)
![Captura15](https://user-images.githubusercontent.com/46933022/202081047-18625cf4-41f4-40f3-b93d-677306df8695.PNG)
![Captura16](https://user-images.githubusercontent.com/46933022/202081053-67cd2b75-91b5-4e17-a365-6cb2b1e64e53.PNG)
![Captura17](https://user-images.githubusercontent.com/46933022/202081059-faef1352-d479-4463-8f49-5aae44ed9840.PNG)
![Captura18](https://user-images.githubusercontent.com/46933022/202081069-2e07162b-3df4-4f5b-a4c1-e062ddf195f7.PNG)
![Captura19](https://user-images.githubusercontent.com/46933022/202081079-ec9e580f-378c-40d3-8833-49395980e4aa.PNG)
![Captura20](https://user-images.githubusercontent.com/46933022/202081085-97fd914e-ffc8-4665-a4ca-4fbca0e231b8.PNG)
![Captura21](https://user-images.githubusercontent.com/46933022/202081091-edc8f2bf-9a15-483a-ae82-5092580e7b9a.PNG)
![Captura22](https://user-images.githubusercontent.com/46933022/202081098-2fb9903d-9e5f-427a-9e8d-c3e9ec60602a.PNG)
![Captura23](https://user-images.githubusercontent.com/46933022/202081104-6527cc97-0409-4703-a5b3-61618dc66873.PNG)
![Captura24](https://user-images.githubusercontent.com/46933022/202081108-97ec97b0-5c66-4359-9f87-60b82302b5b7.PNG)
![Captura25](https://user-images.githubusercontent.com/46933022/202081114-3d847b45-bf2e-46f2-8b0a-b4982b500b69.PNG)

Archivo con los comandos realizados: https://github.com/jcamiloif6/ST0263/blob/main/LAB6/prueba.ipynb


## HIVE y SparkSQL, GESTIÓN DE DATOS VIA SQL

- Ingresar a Hue mediante el link que da el cluster
- Crear la tabla HDI en EMR/S3/Hue/Hive:

  ![imagen](https://user-images.githubusercontent.com/46933022/202083078-991ba814-f1cb-4556-a78c-42f3752cc2f1.png)
  
- Hacer consultas y cálculos sobre la tabla HDI:
  
  ![imagen](https://user-images.githubusercontent.com/46933022/202083417-089b0cea-9fea-4e0e-9b5b-dcfc788b0122.png)

  ![imagen](https://user-images.githubusercontent.com/46933022/202083609-cc369b9a-eb21-476c-820d-5bf43d3d0ef7.png)

  - Crear Tabla Expo

    ![imagen](https://user-images.githubusercontent.com/46933022/202084136-d3bae48d-67bd-4d23-80e5-0a9b0a973477.png)

  - EJECUTAR EL JOIN DE 2 TABLAS:

    ![imagen](https://user-images.githubusercontent.com/46933022/202084392-aea5de68-4b79-44ce-94dc-097b96e0c2fe.png)

- WORDCOUNT EN HIVE:

  - Crear tabla:
  
    ![imagen](https://user-images.githubusercontent.com/46933022/202084858-1379b1ac-d75f-4cd9-b84a-d8faa5943dc5.png)
    
  - Ordenado por palabra
    
    ![imagen](https://user-images.githubusercontent.com/46933022/202085059-c841f2e6-4415-4dd7-9fbf-efb818be42bb.png)
    
  - Ordenado por frecuencia de menor a mayor

  ![imagen](https://user-images.githubusercontent.com/46933022/202085475-9beb5186-e510-4c97-9254-e43846a897bd.png)

  ![imagen](https://user-images.githubusercontent.com/46933022/202085598-fcdadc07-829e-4e65-a984-7aa250e17400.png)

