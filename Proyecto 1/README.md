# ST0263_P1
Proyecto1 Topicos Especiales en Telematica

1. Ubicarse en la carpeta ST0263_P1

```cd ST0263_P1```

2. Instalar los archivos de requirements.txt

```pip install -r requirements.txt```

# Como testear el nodo de BD (Single server)

1. Correr con python el archivo  ST0263_P1/node/main_server.py -p ##, siendo ## un número de puerto 
    por el cual se desee correr el servidor

2. Correr el programa ST0263_P1/main_client.py -h host -p puerto, donde el host se puede dejar en blanco y tomará 
    como predeterminado el localhost o el 127.0.0.1 y el número de puerto se debe indicar el indicado por el servidor

3. Hacer las pruebas que quiera usando los métodos get, set o delete.

# Como testear en modo cluster la BD

1. Correr con python el archivo  ST0263_P1/node/main_server.py -p ##, siendo ## un número de puerto 
    por el cual se desee correr el servidor. Se hace esto para cada nodo

2. Correr con python el archivo  ST0263_P1/node/main_server.py -c ## 'nombre'. Siendo ## el número de puerto que se desee,
    en este puerto estará el servidor de frontend, y 'nombre' un nombre cualquiera que se le debe dar al cluster. Este nombre
    es fundamental para recuperar los datos, ya que con este nombre se almacenan los nodos participes en el sistema de base de 
    datos distribuida.

3. Correr el programa ST0263_P1/main_client.py -h host -p puerto, donde el host se puede dejar en blanco y tomará 
    como predeterminado el localhost o el 127.0.0.1 y el número de puerto se debe indicar el indicado por el servidor. En este caso se especifica el puerto del servidor front-end, los comandos son similares al modo single-node.

## Comando para el main_client.py

- get key -> obtiene el valor especificado por key
- set key value -> almacena value con la clave key
- delete key -> elimina la clave key
- out -> sale del programa cliente

Nota: para ver todos los redireccionamientos de la base de datos redistribuida se puede ver la terminal del servidor front end
    , en este momento solo los envía al último nodo por un problema de hotspots al usar la función hash() de python.

## Documentacion de endpoints con OpenAPI
Mientras el servidor corre abrir el navegador y acceder a
```host:port/docs```

## Arquitectura de la solución

La arquitectura que se presenta es un cliente - servidor básico, donde se tiene un archivo de cliente (main_client.py) que
se conecta a un servidor front-end (main_server.py). Este servidor puede funcionar de dos maneras diferentes:

- Como base de dato en nodo único: recibe las peticiones y las realiza en el mismo servidor.
- Como base de datos distribuida: recibe las peticiones y las reenvía a diferentes nodos que esten conectados al
  servidor.

Para iniciar un modo o el otro se explico en el anterior índice. Un punto cumplido fundamental es la transparencia del 
cliente hacia el servidor, ya que el cliente no tiene manera de saber si el servidor al cual se está conectando se trata
de un nodo único o una base de datos distribuida.

Otro dato importante que merece la pena comentar, es que todas las comunicaciones (cliente servidor y servidor nodos) son
asincrónicas, por lo que se garantiza la consistencia, pero se sacrifica el rendimiento. También trae problemas con la
escalabilidad del proyecto, sin embargo, se trata de una base de datos minimalista con fines educativos.

### Ventajas de la solución implementada

Esta solución que se implementó tiene varias características que podrían sobresalir:

- Se cumple el principio de la transparencia por parte del usuario hacia el servidor.
- Se cumplío el reto del particionamiento de la base de datos, ya que se pudo dividir el almacenamiento en los diferentes
  nodos del sistema.
- Se logró cumplir con la persistencia, ya que al crear cualquier cambio como un set o un delete se almacena la informción
  en un archivo .pickle (serialización del diccionario) en el disco duro del equipo, por si se apaga el servidor y se vuelve
  a encender, se sigue manejando la misma información del último cambio realizado.
