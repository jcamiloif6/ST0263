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



