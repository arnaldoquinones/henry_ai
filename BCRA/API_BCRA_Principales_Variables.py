import requests
import pandas as pd

# URL de la API
url = "https://api.bcra.gob.ar/estadisticas/v2.0/principalesvariables"


# Realizar la solicitud GET
try:
    response = requests.get(url, verify=False)
    response.raise_for_status()  # Verifica si hubo errores en la solicitud

    # Convertir la respuesta JSON a un objeto de Python
    data = response.json()
    
    # Extraer la lista 'results'
    results = data.get("results", [])
    
    # Convertir la lista de diccionarios en un DataFrame
    principalesVariables = pd.DataFrame(results)
    
    # Establecer 'idVariable' como índice
    principalesVariables.set_index("idVariable", inplace=True)
    
    # Mostrar los primeros registros del DataFrame
    print(principalesVariables)

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API: {e}")
except KeyError as e:
    print(f"Error procesando los datos: {e}")

principalesVariables[['cdSerie']+['descripcion']].to_csv('BCRA/principalesVariables.csv')