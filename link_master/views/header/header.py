import reflex as rx
from link_master.styles.styles import Size as size
from link_master.components.info import info
from link_master.styles.colors import TextColor as TextColor
from link_master.components.link_icon import link_icon 
from link_master.styles.colors import TextColor as text_color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="https://th.bing.com/th/id/OIP.w2L9M3-uq-aLObvWnaiFBAHaEK?rs=1&pid=ImgDetMain",
                rows="1",
                spacing="2",
                radius="full",
                size="9",
                padding="1px",
                border="4px solid blue"
                ),
            rx.vstack(
                rx.heading(
                    "Chito Y Cris",
                    size="8",
                    color_scheme="cyan"
                ),
                rx.text(
                    "@chito2.1.2",
                    margin_top="0px !important",
                    color=text_color.AZUL.value
                ),
                rx.hstack(
                    link_icon("https://www.tiktok.com/@chito2.1.2")
                ),
                align_items="start"
            )
        ),
        rx.flex(
            info("+45K ", "Seguidores en TikTok"),
            rx.spacer(),
            info("+600K", "Likes en TikTok"),
            rx.spacer(),
            info("+50", "Recetas!"),
            width="100%",
        ),
        rx.text("""Bienvenidos a la pagina oficial de Chito y Cris, en esta pagina podras encontrar todo el contenido de nuestras
                recetas, ingredientes, y mas detalles!! El contenido estara divido por varias secciones para que encuentres
                facilmente lo que buscas. Si tienes alguna duda o sugerencia no dudes en contactarnos en nuestras redes sociales!"""),
                spacing="7",
                align_items="start",
    )