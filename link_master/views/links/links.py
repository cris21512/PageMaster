import reflex as rx
from link_master.components.link_button import link_button 
from link_master.components.title import title
import link_master.conts as const
from link_master.styles.styles import Size as Size 
from link_master.styles.styles import TextColor as TextColor




def links() -> rx.Component:
    return rx.vstack(
        title("Comunidades"),
        link_button(
            "Twitch",
            "Directos de todo tipo!",
            "/assets/icons/youtube.svg",
            const.TWITCH
        ),
        link_button(
            "Youtube",
            "Video de cocina",
            "/assets/icons/youtube.svg",
            const.YOUTUBE
        ),
        link_button(
            "Canal de Whatsapp",
            "Nuestro canal de whatsapp para estar al tanto de todo!",
            "/assets/icons/youtube.svg",
            const.CDW
        ),

        title(
            rx.text(
            "RECETAS",
            size="8",
            ),
        ),
        rx.text("""A continuación, te presentamos una lista de nuestras recetas dividas
                por sus respectivas categorias. ¡Hechales un vistazo!"""),

                title("Res"),
        link_button(
            "Carne Asada",
            "nuestra receta de carne asada con chimichurri!",
            "/assets/icons/youtube.svg",
            const.ASADO
        ),
        link_button(
            "Fajitas Mar y Tierra",
            "Una explosion de sabores en esta receta!",
            "/assets/icons/youtube.svg",
            const.FAJITAS
        ),
        link_button(
            "Tacos de Res a nuestro estilo!",
            "Una forma sencilla de preparar unos deliciosos tacos!",
            "/assets/icons/youtube.svg",
            const.TACRES
        ),
        link_button(
            "Gringas",
            "Unas Blanquitas, Buenotas he irresistibles... ¡Gringas!",
            "/assets/icons/youtube.svg",
            const.TORHAR
        ),
        link_button(
            "Garnachas",
            "Nuestro etilo de preparar unas deliciosas garnachas!",
            "/assets/icons/youtube.svg",
            const.GARNA
        ),
        link_button(
            "Tacos de Birria",
            "Hay muchas formas de preparar birria, esta es la nuestra!😎",
            "/assets/icons/youtube.svg",
            const.BIRRIA
        ),
        link_button(
            "Lasaña",
            "Una forma muy deliciosa de preparar una lasaña!",
            "/assets/icons/youtube.svg",
            const.LASAÑA
        ),

                title("Pollo"),
        link_button(
            "Pollo Horneado",
            "Un pollo especial para cualquier ocasion especial!",
            "/assets/icons/youtube.svg",
            const.HORNEADO
        ),
        link_button(
            "Pepian",
            "Un platillo tipico de Guatemala, muy delicioso!",
            "/assets/icons/youtube.svg",
            const.PEPIAN
        ),
        link_button(
            "Pollo en Crema",
            "Nuestro pollo en crema es lo mejor de lo mejor!!",
            "/assets/icons/youtube.svg",
            const.POLLOCREMA
        ),
        link_button(
            "Pollo en Freidora de Aire",
            "Si Tienes una freidora de aire, no te puedes perder esta receta!",
            "/assets/icons/youtube.svg",
            const.FREIDORA
        ),

                    title("Cerdo"),
        link_button(
            "Carnitas",
            "Con ganas de carnitas? aqui esta nuetsra receta!!",
            "/assets/icons/youtube.svg",
            const.CARNITAS
        ),
        link_button(
            "Pupusas",
            "Al puro estilo chapin 😎",
            "/assets/icons/youtube.svg",
            const.PUPUSAS
        ),
        link_button(
            "Frijoles Colorados!",
            "Nada que un buen plato de frijoles colorados no pueda arreglar!",
            "/assets/icons/youtube.svg",
            const.FRJOLCOLORADO
        ),
        link_button(
            "Frijoles Colorados (Con Chicharron)",
            "Lo mismo, pero con chicharron😅",
            "/assets/icons/youtube.svg",
            const.CHICHACOLORAO
        ),

                title("Mariscos"),
        link_button(
            "Ceviche",
            "Un ceviche guatemalteco muy delicioso!",
            "/assets/icons/youtube.svg",
            const.CEVICHE
        ),
        link_button(
            "Aguachile🥵",
            "Un Aguachile rojo muy... pero muy... picante!""",
            "/assets/icons/youtube.svg",
            const.AGUACHILE
        ),
        link_button(
            "Mojarras Fritas",
            "No sabes como preparar tus mojarras fritas? aqui te enseñamos!",
            "/assets/icons/youtube.svg",
            const.MOJARRA
        ),
        link_button(
            "Caldo de Mariscos",
            "Nada mejor que un buen caldo de mariscos hecho en casa!",
            "/assets/icons/youtube.svg",
            const.CALDODMARISCOS
        ),
        title(
            rx.text(
            "NO ECUENTRAS LO QUE BUSCAS?",
            size="8",
            ),
        ),
        rx.text("""Puedes ver estas recetas y mas en nuestra cuenta de
                de TikTok!! 👇"""
            ),
        link_button(
            "Nuestro TikTok",
            "MIra toda nuestras recetas aqui!!",
            "/icons/yotube.svg",
            const.TIKTOK
        ),
        width="100%",
    )