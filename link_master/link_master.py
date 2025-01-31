import reflex as rx
from link_master.components.navbar import navbar
from link_master.components.footer import footer
from link_master.views.header.header import header
from link_master.views.links.links import links
import link_master.styles.styles as styles
from link_master.styles.styles import Size as size


class State(rx.State):
    pass 

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=size.BIG.value,
            )
        ),
        footer(),
    )

app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Chito Y cris | Recetas, Viajes, Cultura y mucho mas!!",
)