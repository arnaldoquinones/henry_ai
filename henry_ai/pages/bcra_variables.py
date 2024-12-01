import reflex as rx
from reflex.state import State
from datetime import datetime
from henry_ai.utils.utils import validar_variable, validar_fecha, dividir_rango_fechas
import requests
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Estado global de la aplicación
class AppState(State):
    variable: str = '1'
    fecha_desde: str = None
    fecha_hasta: str = None
    inicio = [2021-1-1]
    final = [2021-1-5]
    tabla = []
    valores = []
    mensaje_error = ''
    data= pd.DataFrame(tabla)
    columnas = []
    @rx.event
    def obtener_datos_concatenados(self):
        """
        Función que consulta la API de BCRA para diferentes rangos de fechas y concatena los resultados en una lista de diccionarios.

        Args:
            variable (str): El identificador de la variable a consultar.
            inicio (list): Lista de fechas iniciales (formato datetime.date o datetime.datetime).
            final (list): Lista de fechas finales correspondientes a los rangos de consulta.

        Returns:
            list: Lista de diccionarios con los datos obtenidos de la API.
        """
        self.mensaje_error = 'Inicio la carga de datos'
        for i, f in zip(self.inicio, self.final):
            url = f"https://api.bcra.gob.ar/estadisticas/v2.0/datosvariable/{self.variable}/{i.strftime('%Y-%m-%d')}/{f.strftime('%Y-%m-%d')}"
            print(i)
            try:
                response = requests.get(url, verify=False)
                response.raise_for_status()  # Verifica si hubo errores en la solicitud

                # Convertir la respuesta JSON a un objeto de Python
                data = response.json()

                # Extraer la lista 'results'
                results = data.get("results", [])

                if results:
                    self.tabla.extend(results)  # Añadir los resultados a la lista de datos
                    self.columnas = [list(dic.keys()) for dic in self.tabla]
                    self.valores = [list(dic.values()) for dic in self.tabla]
                    self.mensaje_error = f'Datos Cargados: columnas: {self.data.columns}'
                    self.data = pd.DataFrame(results)
                    print(results)
                    print(data)

                else:
                    self.mensaje_error = 'No hay datos'

            except requests.exceptions.RequestException as e:
                self.mensaje_error = f'Error: {e}'
            except KeyError as e:
                self.mensaje_error = f'Error: {e}'


    @rx.event
    def validar_inputs(self, variable_input, desde_str, hasta_str):
        """Valida los inputs y actualiza el estado."""
        self.mensaje_error = ""
        # Validar variable
        variable_valida = validar_variable(variable_input)
        if variable_valida is not None:
            self.mensaje_error = f"Variable válida: {variable_input}"
        else:
            self.mensaje_error = "La variable ingresada no es válida. Inténtalo de nuevo."
        
        # Validar fechas
        fecha_desde = validar_fecha(desde_str)
        
        if fecha_desde is not None:
            self.mensaje_error = f"Fecha inicial válida: {desde_str}"
        else:
            self.mensaje_error = "Formato de fecha inicial inválido. Inténtalo de nuevo."

        fecha_hasta = validar_fecha(hasta_str)

        if fecha_hasta is not None:
            self.mensaje_error = f"Fecha final válida: {hasta_str}"
        else:
            self.mensaje_error = "Formato de fecha final inválido. Inténtalo de nuevo."

        # Dividir rango de fechas
        inicio, final = dividir_rango_fechas(desde_str, hasta_str)

        # Actualizar el estado
        self.variable = variable_valida
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.inicio = inicio
        self.final = final
        self.mensaje_error = self.inicio[0]

# Página principal
# Página de validación
def validation_page():
    return rx.center(
        rx.vstack(
            rx.heading("Ingreso de Datos", size="lg"),
            rx.input(
                placeholder="Variable (idVariable)",
                on_change=lambda value: AppState.set_variable(value),
            ),
            rx.input(
                placeholder="Fecha inicial (yyyy-mm-dd)", 
                on_change=lambda value: AppState.set_fecha_desde(value),
            ),
            rx.input(
                placeholder="Fecha final (yyyy-mm-dd)", 
                on_change=lambda value: AppState.set_fecha_hasta(value),
            ),
            rx.button(
                "Aceptar",
                on_click=AppState.validar_inputs(AppState.variable, AppState.fecha_desde, AppState.fecha_hasta),  # Ejecuta el método de validación
            ),
            rx.button(
                "Obtener Datos",
                on_click=AppState.obtener_datos_concatenados(),  # Ejecuta el método de validación
            ),
            
            rx.data_table(
                data= AppState.data,
                pagination= True,

            ),
        ),
            rx.text(AppState.mensaje_error, color="red"),
            rx.link("Volver al inicio", href="localhost:3000", style={"color": "blue", "marginTop": "10px"}),
            
    )

# Configuración de la aplicación
app = rx.App(state=AppState)

app._compile()