## Estudiante: Juan Camilo Iguarán, jciguaranf@eafit.edu.co
## Materia: Topicos especiales de telematica
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 
#
# Lab 5-1-Aws-EMR
# 
# Creacion de cluster
A continuación se detallará paso a paso la creación del cluster emr y la elaboración del lab5-1 como tal. Este laboratorio es realizado en aws y como prerrquisito es necesario tener un par de claves ppk para poder realizar este lab

__1. Click en crear cluster y una vez dentro, click en opciones avanzadas__:    
   ![imagen](https://user-images.githubusercontent.com/46933022/199122606-1dd26263-ac8f-4156-931b-2379739a7b95.png)

__2. Seleccionar emr-6.3.1 y los componentes a utilizar:__      
   ![imagen](https://user-images.githubusercontent.com/46933022/199123143-4a60fd4d-3b2a-4e68-a0aa-46ed039eba68.png)

__3. AWS Glue Data Catalog settings:__   
   ![imagen](https://user-images.githubusercontent.com/46933022/199123402-a44cb7a0-87d7-4554-8755-2b42dc53569e.png)

__4. Edit software settings:__ Para esto nos vamos al siguiente link https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-s3.html y copiamos la configuración que allí aparece y la pegamos en nuestro cluster y le damos next
   ![imagen](https://user-images.githubusercontent.com/46933022/199123860-a579ef2c-0104-411d-8f09-0b3f760109a0.png)
   
   Nota: se debe cambiar el nombre del bucket

__5. Se configuran el tamaño de las instancias en m4.xlarge y en el espacio de opción de compra se señala de tipo Spot:__   
   ![imagen](https://user-images.githubusercontent.com/46933022/199124368-d7ddbf32-3c82-4c1f-b09b-f47c3dac5e16.png)


   ![imagen](https://user-images.githubusercontent.com/46933022/199124271-cb73e8ce-70e7-4102-bc73-ca2e3502310a.png)
   
   No tenemos el nodo de tipo tarea por eso no lo tocamos


__6. Habilitar terminación automática y aumentar almacenamiento en 20Gb y le damos next:__   
   ![imagen](https://user-images.githubusercontent.com/46933022/199124731-8fed762b-bdf4-40e1-85e9-278e70b385f8.png)


__7. Ponemos nombre al cluster y le damos next:__   
   ![imagen](https://user-images.githubusercontent.com/46933022/199124963-48642278-5f9f-4ca6-aa41-6ba17174cec0.png)


__8. Elegimos nuestro par de claves creados previamente como prerequisito y le doy en crear cluster:__   
   ![imagen](https://user-images.githubusercontent.com/46933022/199125129-683f92c4-81e5-406a-89fb-1b72487253d3.png)


__9. Si todo salió bien, se debería ver de la siguiente manera la creación del cluster:__   
   ![imagen](https://user-images.githubusercontent.com/46933022/199125377-a9d5c361-721a-4a6a-892b-31108c4ed192.png)  
Se verifica en la pestaña de cluster que su cluster este en proceso de creacion, esto puede llegar a durar 25 min o mas. 

Así se debe ver una vez el cluster haya terminado de configurarse
![imagen](https://user-images.githubusercontent.com/46933022/199127214-34e45d56-9654-4d4f-adff-e4d51d068f17.png)


# Creacion de bucket
__Pagina Principal de S3 para la creacion de nuestro bucket y le damos crear:__   
   ![imagen](https://user-images.githubusercontent.com/46933022/199127627-63f5deb6-68ce-4e30-abb1-fce05a3121e2.png)

__Creacion del bucket:__ Le ponemos el nombre que le pusimos a la persistencia del notebook cuando estabamos creando el cluster y le damos crear   
  ![imagen](https://user-images.githubusercontent.com/46933022/199127868-0f1d4158-fbbf-46d9-9daa-1e04c7beb6f7.png)
  
__Ingresar al Master con SSH__: Para ingresar al master con ssh simplemente ingresamos a la información del cluster y le damos click donde dice DNS público principal y seguimos las instrucciones
   ![imagen](https://user-images.githubusercontent.com/46933022/199128321-1f09c8d2-7c73-48e4-bb37-74325354c30e.png)

# Configuración de los puertos
  __Para configurar los puertos nos vamos a la opción bloquear acceso público, nos vamos a editar y añadimos los siguienetes puertos__:
  ![imagen](https://user-images.githubusercontent.com/46933022/199131203-fc37b99b-16c5-4e35-9786-79b61171d076.png)

# Configuración de grupos de seguridad
  __1__: Nos vamos al cluster y le damos click al enlace que aparece en grupos de seguridad para principal
  ![imagen](https://user-images.githubusercontent.com/46933022/199131412-13f7522a-4bd9-4d7c-9043-1bc7839bfeba.png)


__DNS para la conexion del master:__   
  ![3](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Bucket/4.png)   
  ![4](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Bucket/5.png)   
  - Comprobe la conexion al master desde dos maquinas diferentes, desde un S.O apple y desde un windows 
  - Nos metemos a el cluster creado y nos conectamos al master medio SSH

__Comandos para verificar el sistema de almacenamiento HDFS:__   
  ![ComandosparasistdeaAlma](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/ComandosparasistdeAlma.png) 

__Ingreso a HUE:__   
  ![configdeHUE](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/configdeHUE.png)   
  Aqui podemos ver que ya entramos al main de HUE y ya se habilitaron los puertos necesarios para la elaboracion de este lab5

__Creacion de archivos DHFS:__   
  ![archivosDHFS](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/archivosDHFS.png)   
  En este SS, se muestra la interfaz de files (DHFS) y como se creo una carpeta llamada datasets para probar esta herramienta

__Creacion de un nuevo bucket en S3:__   
  ![s3NewBucket](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/s3NewBucket.png)   
  Aqui se puede mostrar como se creo un nuevo bucket en la pestaña de S3 llamada datasetssmenesesd, y en este S3 es donde se van a almacenar datos que siempre van a permanecer.

__Ingreso a JupyterHUB:__   
  ![entramosjupyterHUB](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/entramosjupyterHUB.png)   
  Podemos ver que logramos entrar a jupyterHUB y estamos en el login

__Verificacion de Spark en jupyter:__   
  ![verifSpark](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/verifSpark.png)   
  En este SS podemos verificar que en jupyter si esta bien configurado spark.

__Ingreso a zeppelin:__   
  ![mainZeppelin](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/mainZeppelin.png)   
  Verificamos de que sea posible el ingreso a Zeppelin

__Verificamos el uso de spark en zeppelin:__  
  ![zeppelinSpark](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/zeppelinSpark.png)   
  Se ingresan unos comandos a la linea de codigo para verificar el uso de spark en zeppelin.

__Verificacion del archivo prueba en jupyter en S3:__   
  ![verifPruebaS3](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/verifPruebaS3.png)   

__Finalizamos el cluster:__   
  ![finCluster](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/finCluster.png)   
  Y ya por ultimo finalizamos el cluster y si es necesario volver a usarlo, lo clonamos con los mismos ajustes y eso es todo
