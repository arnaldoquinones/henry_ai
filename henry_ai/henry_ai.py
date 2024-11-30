"""AI GEKKO PROYECT."""

import reflex as rx
from rxconfig import config
from reflex import app

# Importa la página de validación
from henry_ai.pages.bcra_variables import validation_page


class State(rx.State):
    """The app state."""
    ...


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
