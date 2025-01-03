import reflex as rx


def info (title: str, body: str) -> rx.Component:
    return rx.box(
        rx.blockquote(
            rx.text(title ,
            size="3",
            color_scheme="blue"),
            
            f"{body}", 
            font_size="8"
        )
    ) 