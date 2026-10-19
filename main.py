
from archivos import cargar_expedientes, generar_archivo_constancia
from expedientes import (
    registrar_expediente,
    buscar_expediente,
    listar_expedientes,
    ordenar_expedientes
)


def mostrar_menu():
    print("\n=== SISTEMA DE MESA DE PARTES ===")
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Listar expedientes")
    print("4. Ordenar expedientes")
    print("5. Generar constancia")
    print("6. Salir")


def generar_constancia(expedientes):
    expediente = buscar_expediente(expedientes)

    if expediente is None:
        return

    nombre_archivo = generar_archivo_constancia(expediente)
    print("Constancia generada:", nombre_archivo)


def main():
    expedientes = cargar_expedientes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_expediente(expedientes)
        elif opcion == "2":
            buscar_expediente(expedientes)
        elif opcion == "3":
            listar_expedientes(expedientes)
        elif opcion == "4":
            ordenar_expedientes(expedientes)
        elif opcion == "5":
            generar_constancia(expedientes)
        elif opcion == "6":
            print("Sistema finalizado.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
