
from datetime import datetime

def validar_texto_obligatorio(texto):
    return texto.strip() != ""

def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False
