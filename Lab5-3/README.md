# Laboratorio 5-3

## Estudiante: Juan Camilo Iguaran - correo: jciguaranf@eafit.edu.co

En el laboratorio 5-3 se utilizara la librería de MRJob python para poder ejecutar el framework de MapReduce, para instalar la librería se debe ejecutar el código de:

```bash
pip install mrjob
```

## Parte 1
Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico. En esta primera parte se ejecutará el dataset de dataempleados.txt

### 1.1 salario anual de los empleados por sector económico
### comando:

```python
python MR1-1.py ./datasets/dataempleados.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200078527-61863f54-f7e3-4220-a102-71191bb7cb06.png)


### 1.2 El salario promedio por Empleado. 
### Comando:

```python
python MR1-2.py ./datasets/dataempleados.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200077757-4f8ea9ac-651b-4ce2-8674-062b2a1c4aa2.png)


### 1.3  Número de SE por Empleado que ha tenido a lo largo de la estadística
### Comando

```python
python MR1-3.py ./datasets/dataempleados.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200078716-e418916b-27f4-4176-be10-dc78bceb1c04.png)


## Parte 2
Se tiene un conjunto de acciones de la bolsa, en la cual se reporta a diario el valor promedio por acción. Para esto se utilizará el dataset de dataempresas.txt

### 2.1  Por acción, dia-menor-valor, día-mayor-valor

```python
python MR2-1.py ./datasets/dataempresas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200079340-c809fa6d-26df-4db5-a9df-47cd99a3641d.png)


### 2.2 Listado de acciones que siempre han subido o se mantienen estables.
### Comando

```python
python MR2-2.py ./datasets/dataempresas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200081447-3e896cb9-d05f-4f89-9bb8-0940a75050ff.png)


### 2.3 DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.
### Comando

```python
python MR2-3.py ./datasets/dataempresas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200079987-8792bfb0-731e-425b-b656-fb8704ccb000.png)


## Parte 3 

### Parte 3.1 Número de películas vista por un usuario, valor promedio de calificación
### Comando

```python
python MR3-1.py ./datasets/datapeliculas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200080216-03b6c78b-da5e-45b5-8a81-91aa3ce0d1c7.png)
![imagen](https://user-images.githubusercontent.com/46933022/200080264-67d2faae-2464-4fde-b53c-3b7f2f40102a.png)


### Parte 3.2 Día en que más películas se han visto
### Comando

```python
python MR3-2.py ./datasets/datapeliculas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200080423-5b457026-216d-451f-88d0-f9071e163805.png)


### Parte 3.3 Día en que menos películas se han visto
### Comando

```python
python MR3-3.py ./datasets/datapeliculas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200080886-e20ba7af-c7f6-408b-92ab-466f2dc2bf1a.png)


### Parte 3.4  Número de usuarios que ven una misma película y el rating promedio
### Comando 

```python
python MR3-4.py ./datasets/datapeliculas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200080978-46d00f6f-43e2-41e2-aee8-4dd4b2d7d377.png)
![imagen](https://user-images.githubusercontent.com/46933022/200081035-d16971a8-1e4a-4a83-b303-d959ef7340f9.png)



### Parte 3.5 Día en que peor evaluación en promedio han dado los usuarios
### Comando

```python
python MR3-5.py ./datasets/datapeliculas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200081114-24daf229-2415-4b7b-951d-af2706c44e02.png)


### Parte 3.6 Día en que mejor evaluación han dado los usuarios
### Comando

```python
python MR3-6.py ./datasets/datapeliculas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200081208-3eebe9d4-e8bb-4400-832d-9b03d27dd6d4.png)


### Parte 3.7 La mejor y peor película evaluada por genero
### Comando

```python
python MR3-7.py ./datasets/datapeliculas.txt
```

![imagen](https://user-images.githubusercontent.com/46933022/200081347-75f37020-f077-40ac-9f43-f46dfb3d281a.png)



