## Estudiante: Juan Camilo Iguarán, jciguaranf@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Proyecto 3 PYSPARK
# 

## Introducción
### Crear entorno

En un archivo ipyin poner las siguientes instrucciones

![imagen](https://user-images.githubusercontent.com/46933022/203354795-638b930e-35da-477c-a2a8-b34fabb93cb1.png)

![imagen](https://user-images.githubusercontent.com/46933022/203354938-563187fa-436a-4692-b019-8294a9d2291b.png)

![Captura2](https://user-images.githubusercontent.com/46933022/203351883-a250e81a-d800-484d-8e85-361f1b8516aa.PNG)

## 0. almacenar datos en AWS S3 y en google drive
- En AWS:

  - ![Captura3](https://user-images.githubusercontent.com/46933022/203352888-c7354e41-a950-41ee-901b-57877bca6c57.PNG)
  
- En Drive

 - ![Captura4](https://user-images.githubusercontent.com/46933022/203353052-e04df2fa-a4cd-4a6d-bad8-3e8db8d0cc8d.PNG)
 
 - ![imagen](https://user-images.githubusercontent.com/46933022/203353453-33da42fb-8c6f-414b-87d0-4a3bd17e32b9.png)

## 1. cargar datos desde AWS S3 y desde google drive.

![imagen](https://user-images.githubusercontent.com/46933022/203355450-bedb074b-41ff-4cb1-822c-eef0dad8fc79.png)


## 2. Análisis exploratorio del dataframe donde cargamos los datos:
## 2.1 columnas

![Captura7](https://user-images.githubusercontent.com/46933022/203356216-e7c470a2-fe93-41df-98ec-efb0338fe01f.PNG)

## 2.2 tipos de datos

![Captura8](https://user-images.githubusercontent.com/46933022/203356334-5c42a06b-78e7-4be3-af9f-692295314e68.PNG)

## 2.3 seleccionar algunas columnas

![Captura9](https://user-images.githubusercontent.com/46933022/203356459-d5da8582-4cb7-4822-9620-5f16a98f0855.PNG)

## 2.4 RENOMBRAR COLUMNAS (esto se recomienda hacerlo para facilitar el procesamiento posterior)

![Captura10](https://user-images.githubusercontent.com/46933022/203356555-fb0c94e4-89d9-4e30-9286-0a85e1112518.PNG)

## 2.5 agregar columnas

![Captura11](https://user-images.githubusercontent.com/46933022/203356812-de14ea6c-70d5-4af8-87bd-e1e34bc31cc3.PNG)

![Captura12](https://user-images.githubusercontent.com/46933022/203356850-f739b2f0-d19d-4daf-9557-7a5f94c56bf2.PNG)

## 2.6 borrar columnas

![Captura13](https://user-images.githubusercontent.com/46933022/203356988-b4396064-9208-411c-840e-e0f9464b6f32.PNG)

## 2.7 filtrar datos

![Captura14](https://user-images.githubusercontent.com/46933022/203357129-68b0019c-0f7a-4a75-bb44-901a02de343e.PNG)

![Captura15](https://user-images.githubusercontent.com/46933022/203357192-85156f20-ef3a-400f-b482-eb440e1d9256.PNG)

##  2.8 ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva.

![Captura16](https://user-images.githubusercontent.com/46933022/203357428-ca59b4a4-daec-4611-91db-f092c341c875.PNG)



## 3. contestar las siguientes preguntas sobre los datos de covid:
## 3.1 Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor.

![Captura17](https://user-images.githubusercontent.com/46933022/203358211-9c121a49-d610-4a99-b7d4-04b6324406d4.PNG)

## 3.2 Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor.

![Captura18](https://user-images.githubusercontent.com/46933022/203358379-06841031-ec22-40d8-8c20-f6b6f17b3b58.PNG)

## 3.3 Los 10 días con más casos de covid en Colombia ordenados de mayor a menor.

![Captura19](https://user-images.githubusercontent.com/46933022/203358484-067e9d29-9dba-4912-a118-176d1dc38534.PNG)

![Captura20](https://user-images.githubusercontent.com/46933022/203358538-671840f0-3b20-49c0-ac8c-7de9971a07c0.PNG)

## 3.4 Distribución de casos por edades de covid en Colombia.

![Captura21](https://user-images.githubusercontent.com/46933022/203358679-c11bd445-44a4-4f79-9a45-7d6e9c00a736.PNG)

## 3.5 Realice la pregunda de negocio que quiera sobre los datos y respondala con la correspondiente programación en spark.

![Captura22](https://user-images.githubusercontent.com/46933022/203358860-92ec3f2f-a6ff-4ff8-b622-2dce786e7123.PNG)
