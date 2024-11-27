"""AI GEKKO PROYECT."""

import requests
from bs4 import BeautifulSoup

# URL de la página
url = "https://dolarhoy.com/"

# Realizar la solicitud GET
response = requests.get(url)
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscar todos los valores de cotización
    values = soup.find_all('div', class_='val')

    if len(values) >= 2:  # Verifica que haya al menos dos valores
        # Extraer e imprimir los primeros dos valores con los títulos asignados
        print("Precios del dólar Blue:")
        print(f"Valor de compra: {values[0].text.strip()}")
        print(f"Valor de venta: {values[1].text.strip()}")
    else:
        print("No se encontraron suficientes valores de cotización en la página.")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
