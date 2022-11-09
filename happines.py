import csv
import re

# 1. Descargar el archivo happines.csv, abrirlo con python e imprimir todas las filas
with open("happines.csv", newline="") as happinesFile:
    happinesData = csv.reader(happinesFile, delimiter=";")
    suma = 0
    contador = 0
    # 3. Imprimir solamente la informacion de latinoamerica
    for row in happinesData:
        if row[1] == 'Latin America and Caribbean':
            print(row)
            suma = suma + float(row[3])
            contador = contador + 1

    promedio = suma / contador
    print('promedio', promedio)
