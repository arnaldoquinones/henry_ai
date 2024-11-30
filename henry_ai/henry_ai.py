"""AI GEKKO PROYECT."""

import reflex as rx
from rxconfig import config
from reflex import app
import random

# Importa la página de validación
from henry_ai.pages.bcra_variables import validation_page


class State(rx.State):
    """The app state."""
    ...
class AreaState(rx.State):
    # Define datos iniciales
    data = [
        {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
        {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
        {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
        {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
        {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
        {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
        {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
    ]
    curve_type = "basis"

    @rx.event
    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

    def change_curve_type(self, type_input):
        self.curve_type = type_input


def area_sync() -> rx.Component:
    """Componente que incluye gráficos sincronizados (solo área y línea)."""
    return rx.vstack(
        rx.recharts.composed_chart(
            rx.recharts.area(
                data_key="uv",
                stroke="#2E8B57",
                fill="#2E8B57",
            ),
            rx.recharts.line(
                data_key="pv",
                type_="monotone",
                stroke="#FF0000",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.graphing_tooltip(),
            rx.recharts.brush(
                data_key="name", height=30, stroke="#2E8B57"
            ),
            data=AreaState.data,  # Usa los datos del estado
            sync_id="1",
            width="100%",
            height=200,
        ),
        width="25%",  # Ajusta el tamaño del contenedor
        padding="10px",  # Añade espacio interno
        position="absolute",  # Habilita el desplazamiento absoluto
        top="375px",  # Ajusta la posición vertical (hacia abajo o hacia arriba)
        left="55px",  # Ajusta la posición horizontal (hacia la derecha o izquierda)
        background_color="transparent",  # Fondo para visibilidad
        border_radius="8px",  # Bordes redondeados
        box_shadow="3xl",  # Añade sombra
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.container(
            rx.vstack(
                # Imagen del logo, posicionada de forma independiente
                rx.box(
                    rx.image(
                        src="https://github.com/arnaldoquinones/henry_ai/blob/master/assets/logo_II.png?raw=true",
                        width="300px",
                        height="210px",
                        alt="Logo",
                    ),
                    position="absolute",
                    top="90px",
                    left="90px",
                ),
                # area_chart_component(),
                area_sync(),
                # Texto del encabezado "Welcome to AI Gekko!"
                rx.box(
                    rx.heading("Welcome to AI Gekko!", size="8", color="white"),
                    position="absolute",
                    top="20px",  # Ajusta hacia abajo
                    left="550px",  # Ajusta hacia la derecha
                ),
                rx.box(
                    rx.text("Finanzas", size="8", color="white"),
                    position="absolute",
                    top="365px",  # Ajusta hacia abajo
                    left="535px",  # Ajusta hacia la derecha
                ),
                rx.box(
                    rx.text("Economia", size="8", color="white"),
                    position="absolute",
                    top="365px",  # Ajusta hacia abajo
                    left="800px",  # Ajusta hacia la derecha
                ),
                rx.box(
                    rx.text("Activo", size="8", color="white"),
                    position="absolute",
                    top="330px",  # Ajusta hacia abajo
                    left="200px",  # Ajusta hacia la derecha
                ),
                rx.box(
                    rx.text("Cotizaciones", size="8", color="white"),
                    position="absolute",
                    top="355px",  # Ajusta hacia abajo
                    left="1100px",  # Ajusta hacia la derecha
                ),
                rx.box(
                    rx.text("AI CHAT", size="8", color="white"),
                    position="absolute",
                    top="14px",  # Ajusta hacia abajo
                    left="1035px",  # Ajusta hacia la derecha
                ),
                # Enlace "Ir a Validación"
                rx.box(
                    rx.link(
                        "Ir a Validación",
                        href="/bcra-variables",
                        style={
                            "color": "white",
                            "backgroundColor": "transparent",
                            "padding": "10px",
                            "borderRadius": "5px",
                            "textDecoration": "none",
                        },
                    ),
                    position="absolute",
                    top="22px",  # Ajusta la posición desde la parte superior
                    left="1180px",  # Ajusta la posición desde la izquierda
                ),
            ),
        ),
        background_image="url('https://github.com/arnaldoquinones/henry_ai/blob/master/assets/fondo_dashboard_nuevo_II.jpg?raw=true')",
        background_size="cover",
        background_position="center",
        min_height="100vh",
        position="relative",  # Define el contexto para los elementos con posición absoluta
    )




# Define global styles
style = {
    "::selection": {"background_color": "green"},
    rx.text: {"font_family": "calibri"},
    rx.heading: {"font_weight": "500"},
}

# Create the app with styles
app = rx.App(style=style)

# Add pages to the app
app.add_page(index, route="/")
app.add_page(validation_page, route="/bcra-variables")

# Run the app
app._compile()
