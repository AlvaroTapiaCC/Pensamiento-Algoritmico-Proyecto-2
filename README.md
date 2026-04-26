# Documentacion del programa

## Estructura

`procesar.py` procesa el archivo datos.txt guardado en la carpeta datos, y serializa los datos en un archivo .json o .pkl   
`consultas.py` realiza las consultas, accediendo a las funciones definidas y escribiendo respuestas en un archivo .txt 

## Ejecucion

### Ejecucion normal

python consultas.py "nombre-archivo-consultas" "nombre-archivo-respuestas"

### Simulacion de competencia (WSL)

ulimit -v 4000000 && /usr/bin/time -v taskset -c 0 python3 consultas.py consultas.txt resultados.txt

`Maximum resident set size (kbytes)` muestra el maximo de memoria utilizado
