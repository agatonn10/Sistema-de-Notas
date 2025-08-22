import campers

def menu_principal():
    while True:
        print("========CAMPUSLANDS========")
        print("1) Registrar Camper")
        print("2) Listar Campers")
        print("3) Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            campers.registrar_camper()
        elif opcion == "2":
            campers.listar_campers()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("❌ Seleccione una opcion valida de Campus...")

if __name__ == "__main__":
    menu_principal()