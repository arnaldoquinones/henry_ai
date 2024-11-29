import reflex as rx
from reflex.state import State
from datetime import datetime
from henry_ai.utils.utils import validar_variable, validar_fecha, dividir_rango_fechas

# Estado global de la aplicación
class AppState(State):
    variable: str = None
    fecha_desde: str = None
    fecha_hasta: str = None
    inicio = []
    final = []
    mensaje_error = ""

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
        self.mensaje_error = "✔"

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
        ),
            rx.text(AppState.mensaje_error, color="red"),
            rx.link("Volver al inicio", href="localhost:3000", style={"color": "blue", "marginTop": "10px"}),
        
    )

# Configuración de la aplicación
app = rx.App(state=AppState)

app._compile()