from enum import Enum
import reflex as rx
from .colors import Colors as colors
from .colors import TextColor as TextColor 
from .fonts import Font as Font


#Constants
MAX_WIDTH = "600px"

#Enums
class Size(Enum):
    SMALL="0.5em"
    MEDIUM="1em"
    DEFAULT="1.25em"
    COMPACT="1.5em"
    BIG="3em"
    VERY_BIG="4em"

#Styles

BASE_STYLE = {
    "font_family": Font.TEXT.value,
    "background_color": colors.OSCURO.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.OSCURO.value,
        "background_color": colors.PRIMARY.value,
        "border": colors.RED.value,
        "_hover": {
            "background_color": colors.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration":"none",
        "_hover": {}
    }
}

navbar_title_style= dict(
    font_family=Font.TITLE.value,
)


title_style= dict(
    font_family=Font.TITLE.value,
    width="100%",
    padding_top= Size.DEFAULT.value,
    color= TextColor.CYAN.value
)


button_title_style= dict(
    font_family=Font.OSWALD.value,
    font_size=Size.COMPACT.value,
    color= TextColor.OSCURO.value
)

button_body_style= dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    color= TextColor.HEADER.value
)