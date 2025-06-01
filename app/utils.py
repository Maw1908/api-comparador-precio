import json
from pathlib import Path

PRECIOS_PATH = Path(__file__).parent / "precios_guardados.json"

def leer_precios():
    if not PRECIOS_PATH.exists():
        return {}
    with open(PRECIOS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_precios(datos):
    with open(PRECIOS_PATH, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
