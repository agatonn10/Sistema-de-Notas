import json

ARCHIVO_DATOS = "Data/base_datos.json"

def guardado(data):
    """Guarda datos en el JSON"""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def cargar_datos():
    """Carga datos desde el JSON si existe y es válido"""
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                return {}
            return json.loads(contenido)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

#cargar datos al importar el módulo
Datos = cargar_datos()

def actualizar_datos(nuevos_datos):
    """Actualiza los datos en memoria y guarda en JSON"""
    global Datos
    Datos.update(nuevos_datos)
    guardado(Datos)
