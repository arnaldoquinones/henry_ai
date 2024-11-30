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
                # Ajustamos la posición del texto "Welcome to AI Gekko!"
                rx.box(
                    rx.heading("Welcome to AI Gekko!", size="8", color="white"),
                    position="absolute",  # Permite posicionamiento absoluto
                    top="10px",  # Ajusta la posición desde la parte superior
                    left="550px",  # Aumenta este valor para mover más hacia la derecha
                    text_align="center",
                ),
                rx.text(
                    "Get started with investing!! ",
                    size="5",
                ),
                rx.text("Haz clic en el botón para ir a la página de validación."),
                rx.link(
                    "Ir a Validación",
                    href="/bcra-variables",  # Ruta de la segunda página
                    style={
                        "color": "white",
                        "backgroundColor": "green",
                        "padding": "10px",
                        "borderRadius": "5px",
                        "textDecoration": "none",
                    },
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        ),
        background_image="url('https://github.com/arnaldoquinones/henry_ai/blob/master/assets/fondo_dashboard_nuevo_II.jpg?raw=true')",
        background_size="cover",
        background_position="center",
        min_height="100vh",
        position="relative",  # Necesario para que el hijo con posición absoluta funcione
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
