
import csv
import os

ARCHIVO = "expedientes.csv"
CAMPOS = ["codigo", "dni", "nombre", "fecha", "asunto", "area"]

def cargar_expedientes():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def guardar_expedientes(expedientes):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(expedientes)

def generar_archivo_constancia(expediente):
    nombre_archivo = expediente["codigo"] + ".txt"

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("CONSTANCIA DE RECEPCION\n")
        archivo.write("======================\n")

        for campo, valor in expediente.items():
            archivo.write(f"{campo.capitalize()}: {valor}\n")

    return nombre_archivo
