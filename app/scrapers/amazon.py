import requests
from bs4 import BeautifulSoup

def obtener_precio(nombre_producto):
    url = f"https://www.amazon.com/s?k={nombre_producto.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    precios = []
    for item in soup.select(".a-price .a-offscreen"):
        precios.append(item.get_text())
    return precios if precios else ["No encontrado"]
