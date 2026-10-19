from validaciones import (
    validar_texto_obligatorio,
    validar_dni,
    validar_fecha
)
from archivos import guardar_expedientes

def registrar_expediente(expedientes):
    print("\n--- REGISTRO DE EXPEDIENTE ---")

    dni = input("DNI: ").strip()
    nombre = input("Nombre del ciudadano: ").strip()
    fecha = input("Fecha (DD/MM/AAAA): ").strip()
    asunto = input("Asunto: ").strip()
    area = input("Area de destino: ").strip()

    if not all([
        validar_texto_obligatorio(dni),
        validar_texto_obligatorio(nombre),
        validar_texto_obligatorio(fecha),
        validar_texto_obligatorio(asunto),
        validar_texto_obligatorio(area)
    ]):
        print("Error: todos los campos son obligatorios.")
        return

    if not validar_dni(dni):
        print("Error: el DNI debe contener 8 digitos.")
        return

    if not validar_fecha(fecha):
        print("Error: la fecha no es válida.")
        return

    numero = max(
        [int(e["codigo"].split("-")[1]) for e in expedientes],
        default=0
    ) + 1

    expediente = {
        "codigo": f"EXP-{numero:04d}",
        "dni": dni,
        "nombre": nombre,
        "fecha": fecha,
        "asunto": asunto,
        "area": area
    }

    expedientes.append(expediente)
    guardar_expedientes(expedientes)

    print("Expediente registrado:", expediente["codigo"])

def buscar_expediente(expedientes):
    codigo = input("Codigo del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print(expediente)
            return expediente

    print("No se encontro el expediente.")
    return None

def listar_expedientes(expedientes):
    if not expedientes:
        print("No hay expedientes registrados.")
        return

    for expediente in expedientes:
        print(expediente)

def ordenar_expedientes(expedientes):
    expedientes.sort(key=lambda e: e["codigo"])
    guardar_expedientes(expedientes)
    print("Expedientes ordenados por codigo.")
