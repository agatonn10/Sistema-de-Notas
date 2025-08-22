import campers
import rutas

def menu_principal():
    while True:
        print("========CAMPUSLANDS========")
        print("1) Registrar Camper")
        print("2) Listar Campers")
        print("3) Crear Ruta")
        print("4) Listar Rutas")
        print("10) Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            campers.registrar_camper()
        elif opcion == "2":
            campers.listar_campers()
        elif opcion == "3":
            rutas.crear_ruta()
        elif opcion == "4":
            rutas.listar_rutas()
        elif opcion == "10":
            print("Saliendo...")
            break
        else:
            print("❌ Seleccione una opcion valida de Campus...")

if __name__ == "__main__":
    menu_principal()
