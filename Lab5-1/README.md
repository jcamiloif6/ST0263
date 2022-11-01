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



__DNS para la conexion del master:__     
  ![4](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Bucket/5.png)   
  - Comprobe la conexion al master
  - Nos metemos a el cluster creado y nos conectamos al master medio SSH

__Comandos para verificar el sistema de almacenamiento HDFS:__   
  ![ComandosparasistdeaAlma](https://raw.githubusercontent.com/smenesesd/TopicosTelematica/main/Lab5/Lab5-1/img/Cluster/ComandosparasistdeAlma.png) 
  
# Configuración de grupos de seguridad
  __1__: Nos vamos al cluster y le damos click al enlace que aparece en grupos de seguridad para principal
  ![imagen](https://user-images.githubusercontent.com/46933022/199131412-13f7522a-4bd9-4d7c-9043-1bc7839bfeba.png)
  
  __2__: Habilitamos los puertos
   ![Captura1](https://user-images.githubusercontent.com/46933022/199135870-2cd270df-fb40-48e0-801e-d0a9b47629d3.PNG)

# Ingreso a HUE
  __Creamos usuario hadoop__
  
   ![Captura2](https://user-images.githubusercontent.com/46933022/199135986-d2531ec6-5ad9-4c2a-a846-24290072dd3d.PNG)
   
  __Base de datos por defecto__
  
  ![Captura3](https://user-images.githubusercontent.com/46933022/199136119-9c7da4cb-754c-4917-896e-819b101688bc.PNG)
  
  __Archivos creados en hue__:
  
  ![Captura9](https://user-images.githubusercontent.com/46933022/199136755-199fa230-7a19-4582-9f9f-64d976d9bbe6.PNG)


# Ingreso a Jupyterhub
![Captura4](https://user-images.githubusercontent.com/46933022/199136264-3c456e82-5c1d-4cdd-9ab1-f31fec6783d5.PNG)

__Iniciamos Spark__ 

![Captura6](https://user-images.githubusercontent.com/46933022/199136467-e90f7b7c-fae9-40bd-9c32-ecbbc02fa289.PNG)

# Ingreso a Zeppelin
![Captura7](https://user-images.githubusercontent.com/46933022/199136564-c22c328a-c8e3-4c61-923c-3c7692af4a59.PNG)

__Iniciamos Spark__

![Captura8](https://user-images.githubusercontent.com/46933022/199136618-ec0a3580-a036-497a-8db2-c81ca0a5df11.PNG)


# Terminamos el cluster  
  ![Captura10](https://user-images.githubusercontent.com/46933022/199136820-af1f81bf-dca1-4aab-b3a4-93a5af239bff.PNG)

