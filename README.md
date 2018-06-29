# Data Set Generator

El programa registra en un txt qué tecla y cuándo fue apretada y soltada.

## Uso
Para usar el programa existen dos opciones, el ejecutable o el código python. En ambos se debe indicar la carpeta donde se va a guardar data set y el usuario. 

Ejecutable : `./dataSetGenerator <carpeta> <usuario>`

Python: `python3 dataSetGenerator.py <carpeta> <usuario>`

Para terminar de recolectar datos se debe apretar la tecla escape (Esc). Luego, indicar si el data set creado es o no válido, si no es válido se borrará el archivo txt (En caso de pruebas o si hay demasiados errores). 

## Requerimientos

1) Para ejecutar el programa usando el código fuente se necesita usar python 3, además se necesita tener la libreria pynput

    `pip3 install --user pynput`

2) El ejecutable esta hecho para linux de 64 bits. 
