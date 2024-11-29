import pandas as pd
from datetime import datetime, timedelta
import os

# Cargar el DataFrame de principalesVariables
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "data/principalesVariables.csv")
principales_variables = pd.read_csv(csv_path)

def validar_variable(variable_input):
    """Valida si la variable está en la columna idVariable."""
    try:
        variable_input = int(variable_input)
        if variable_input in principales_variables["idVariable"].values:
            return variable_input
        else:
            return None
    except ValueError:
        return None

def validar_fecha(fecha_str):
    """Valida si una fecha está en formato yyyy-mm-dd."""
    try:
        return datetime.strptime(fecha_str, "%Y-%m-%d")
    except ValueError:
        return None

def dividir_rango_fechas(desde, hasta):
    """Divide un rango de fechas en segmentos de hasta un año."""
    inicio = []
    final = []
    fecha_actual = datetime.strptime(desde, "%Y-%m-%d")
    while fecha_actual < datetime.strptime(hasta, "%Y-%m-%d"):
        siguiente = min(fecha_actual + timedelta(days=365), datetime.strptime(hasta, "%Y-%m-%d"))
        inicio.append(fecha_actual)
        final.append(siguiente)
        fecha_actual = siguiente + timedelta(days=1)
    return inicio, final
