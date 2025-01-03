import reflex as rx
import link_master.styles.styles as styles

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="instagram",
            stroke_width="2",
            color="orange",
        ),
        href=url,
        is_external=True
    )