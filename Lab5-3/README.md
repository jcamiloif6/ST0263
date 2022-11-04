# Laboratorio 5-3

## Estudiante: Juan Camilo Iguaran - correo: jciguaranf@eafit.edu.co

En el laboratorio 5-3 se utilizara la librería de MRJob python para poder ejecutar el framework de MapReduce, para instalar la librería se debe ejecutar el código de:

```bash
pip install mrjob
```

## Parte 1
Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico. En esta primera parte se ejecutará el dataset de dataempleados.txt

### 1.1
El salario promedio por Sector Económico (SE). Para ejecutar este código se usa el comando:

```python
python MR1-1.py ./datasets/dataempleados.txt
```

### 1.2
El salario promedio por Empleado. Para ejecutar este código se usa el comando:

```python
python MR1-2.py ./datasets/dataempleados.txt
```

### 1.3
Número de SE por Empleado que ha tenido a lo largo de la estadística. Para ejecutar este código se usa el comando:

```python
python MR1-3.py ./datasets/dataempleados.txt
```

## Parte 2
Se tiene un conjunto de acciones de la bolsa, en la cual se reporta a diario el valor promedio por acción. Para esto se utilizará el dataset de dataempresas.txt

### 2.1
Por acción, dia-menor-valor, día-mayor-valor. Para ejecutar este código se usa el comando:

```python
python MR2-1.py ./datasets/dataempresas.txt
```

### 2.2
Listado de acciones que siempre han subido o se mantienen estables. Para ejecutar este código se usa el comando:

```python
python MR2-2.py ./datasets/dataempresas.txt
```

### 2.3
DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.. Para ejecutar este código se usa el comando:

```python
python MR2-3.py ./datasets/dataempresas.txt
```

## Parte 3
Se tiene un conjunto de datos en el cual se evalúan las películas con un rating. Para esta última parte se utilizará el dataset de datapeliculas.txt

### Parte 3.1
Número de películas vista por un usuario, valor promedio de calificación. Para ejecutar este código se usa el comando:

```python
python MR3-1.py ./datasets/datapeliculas.txt
```

### Parte 3.2
Día en que más películas se han visto. Para ejecutar este código se usa el comando:

```python
python MR3-2.py ./datasets/datapeliculas.txt
```

### Parte 3.3
Día en que menos películas se han visto. Para ejecutar este código se usa el comando:

```python
python MR3-3.py ./datasets/datapeliculas.txt
```

### Parte 3.4
Número de usuarios que ven una misma película y el rating promedio. Para ejecutar este código se usa el comando:

```python
python MR3-4.py ./datasets/datapeliculas.txt
```

### Parte 3.5
Día en que peor evaluación en promedio han dado los usuarios. Para ejecutar este código se usa el comando:

```python
python MR3-5.py ./datasets/datapeliculas.txt
```

### Parte 3.6
Día en que mejor evaluación han dado los usuarios. Para ejecutar este código se usa el comando:

```python
python MR3-6.py ./datasets/datapeliculas.txt
```

### Parte 3.7
La mejor y peor película evaluada por genero. Para ejecutar este código se usa el comando:

```python
python MR3-7.py ./datasets/datapeliculas.txt
```
