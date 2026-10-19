def mostrar_menu():
    print("\n=== SISTEMA DE MESA DE PARTES ===")
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Listar expedientes")
    print("4. Ordenar expedientes")
    print("5. Generar constancia")
    print("6. Salir")
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            print("Funcion de registro pendiente.")
        elif opcion == "2":
            print("Funcion de busqueda pendiente.")
        elif opcion == "3":
            print("Funcion de listado pendiente.")
        elif opcion == "4":
            print("Funcion de ordenamiento pendiente.")
        elif opcion == "5":
            print("Funcion de constancia pendiente.")
        elif opcion == "6":
            print("Sistema finalizado.")
            break
        else:
            print("Opcion no valida.")
if __name__ == "__main__":
    main()
