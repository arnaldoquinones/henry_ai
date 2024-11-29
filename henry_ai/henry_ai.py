"""AI GEKKO PROYECT."""

import reflex as rx
from rxconfig import config
from reflex import app, theme
from henry_ai.pages.bcra_variables import validation_page
class State(rx.State):
    """The app state."""
    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.heading("Welcome to AI Gekko!", size="9", color ="white"),
                rx.text(
                    "Get started with investing!! ",
                    # rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                rx.text("Haz clic en el botón para ir a la página de validación."),
                rx.link(
                    "Ir a Validación",
                    href="bcra_variables.py",  # Ruta de la segunda página
                    style={"color": "white", "backgroundColor": "blue", "padding": "10px", "borderRadius": "5px", "textDecoration": "none"},
                ),

                spacing="5",
                justify="center",
                min_height="85vh",
            ),
            rx.logo(),
        ),
        # Aplicamos el degradado al fondo del contenedor principal
        background_image="linear-gradient(to bottom, #2E8A5E, #A7D4B6)",  # Degradado verde
        background_size="cover",  # Para cubrir toda el área visible
        background_position="center",
        min_height="100vh",  # Asegúrate de que ocupe toda la pantalla
    )

# Define global styles (puedes mantener esto para otros componentes)
style = {
    "::selection": {"background_color": "blue"},
    ".some-css-class": {"text_decoration": "underline"},
    "#special-input": {"width": "20vw"},
    rx.text: {"font_family": "calibri"},
    rx.divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    rx.heading: {"font_weight": "500"},
    rx.code: {"color": "green"},
}

# Create the app with styles
app = rx.App(style=style)

# Add pages to the app
app.add_page(index)
# Agregar la página de validación
app.add_page(validation_page, route="bcra_variables.py")

# Run the app
app._compile()
