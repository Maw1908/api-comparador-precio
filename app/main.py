from fastapi import FastAPI, Query
from app.scrapers import mercadolibre, amazon
from app import utils

app = FastAPI()

@app.get("/comparar-precio")
def comparar_precio(nombre_producto: str = Query(...)):
    precios_actuales = {
        "mercadolibre": mercadolibre.obtener_precio(nombre_producto),
        "amazon": amazon.obtener_precio(nombre_producto),
    }
    precios_previos = utils.leer_precios()
    cambios = {}

    precios_guardados = precios_previos.get(nombre_producto, {})
    actualizado = False

    for tienda, precio_actual in precios_actuales.items():
        precio_actual_simple = precio_actual[0] if isinstance(precio_actual, list) else precio_actual

        if precios_guardados.get(tienda) != precio_actual_simple:
            cambios[tienda] = {
                "antes": precios_guardados.get(tienda),
                "ahora": precio_actual_simple
            }
            precios_guardados[tienda] = precio_actual_simple
            actualizado = True

    if actualizado:
        precios_previos[nombre_producto] = precios_guardados
        utils.guardar_precios(precios_previos)

    return {
        "precios_actuales": precios_actuales,
        "cambios": cambios
    }
