import reflex as rx
import datetime
from link_master.styles.styles import Size as size
import link_master.conts as const


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="https://th.bing.com/th/id/OIP.w2L9M3-uq-aLObvWnaiFBAHaEK?rs=1&pid=ImgDetMain",
            alt="Chito y Cris",
            height=size.BIG.value,
        ),
        rx.link(
            f"© 2023-{datetime.date.today().year} Chito y Cris | Todos los derechos reservados.",
            href="https://www.tiktok.com/@chito2.1.2",
            is_external=True,
            font_size=size.MEDIUM.value,
        ),
        rx.text("Creadores de contenido."),
        margin_bottom=size.BIG.value,
    )
