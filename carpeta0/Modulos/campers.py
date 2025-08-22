from data import Datos, guardado

def registrar_camper():
    camper = {
        "id": input("Ingrese ID: "),
        "nombres": input("Ingrese nombres: "),
        "apellidos": input("Ingrese apellidos: "),
        "direccion": input("Ingrese dirección: "),
        "acudiente": input("Ingrese acudiente: "),
        "telefono": input("Ingrese teléfono: "),
        "estado": "Inscrito",
        "riesgo": "Ninguno"       
    }
    Datos["campers"].append(camper)
    guardado(Datos)
    print("✅ El camper a sido registrado exitosamente.")

def listar_campers():
    if not Datos["campers"]:
        print("⚠️ El camper no a sido registrado.")
    for c in Datos["campers"]:
        print(f"{c['id']} - {c['nombres']} {c['apellidos']} - Estado: {c['estado']}")