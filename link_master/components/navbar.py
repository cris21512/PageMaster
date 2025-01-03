import reflex as rx
from link_master.styles.styles import Size as size
from link_master.styles.styles import colors as colors


def navbar() -> rx.Component:
    return rx.vstack(
        rx.text(
            rx.hstack(
            "Pagina oficial de: Chito y Cris!",
            rx.spacer(),
            "Made by: Master",
            color=colors.CYAN.value,
            font_family="Birthstone-Regular",
            )
        ),
        positions="sticky",
        bg=colors.BLACK.value,
        padding_x=size.BIG.value,
        padding_y=size.SMALL.value,
        z_index="999",
        top="0",
    )