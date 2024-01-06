# EspiralUllam-Python

Implementación de la Espiral de Ullam con matrices NxN en Python.
Tiene funciones para pintar la matriz por terminal, pero sin formato, y también para generar un fichero a partir de un DataFrame de Pandas, asignando el color rojo a los números primos de la matriz.

Como argumentos recibe el tamaño de la matriz y el nombre del fichero para guardar la imagen generada. 
Si no se introduce el tamaño o el nombre se usara el tamaño 3x3 y el nombre de fichero imagen.

Ejemplo:
```
python3 main.py 5 matriz5
```

Ejemplo de imagen generada para matriz de 5x5:

![matriz5](https://github.com/digitaldav/EspiralUllam-Python/assets/4304461/7605aeae-0d57-4326-81ab-f09ef4412937)


Librerias necesarias:
* numpy
* pandas
* dataframe_image

Puede ser necesario instalar Chrome para que funcione dataframe_image.
