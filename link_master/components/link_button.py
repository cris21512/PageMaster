import reflex as rx
from link_master.styles.styles import Size as Size
import link_master.styles.styles as styles


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow-big-right-dash",
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="1",
                    align_items="start",
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
