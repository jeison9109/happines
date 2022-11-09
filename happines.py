import csv

# 1. Descargar el archivo happines.csv, abrirlo con python e imprimir todas las filas
with open("happines.csv", newline="") as happinesFile:
    happinesData = csv.reader(happinesFile, delimiter=";")
    for row in happinesData:
        print(row)
