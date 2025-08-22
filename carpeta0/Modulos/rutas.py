from data import Datos, guardado

def crear_ruta():
    nombre = input("Nombre de la ruta: ")
    modulos = [
        "Fundamentos de programacion",
        "Programacion Web",
        "Programacion formal",
        "Bases de datos",
        "Backend"
    ]
    ruta = {
        "nombre": nombre,
        "modulos": modulos,
        "capacidad": 33
    }
    Datos["rutas"].append(ruta)
    guardado(Datos)
    print("✅ La ruta fue creada exitosamente")

def listar_rutas():
    if not Datos["rutas"]:
        print("⚠️ La ruta no fue creada")
    for r in Datos["rutas"]:
        print(f"Ruta: {r["nombre"]} - Capacidad: {r["capacidad"]} campers")
