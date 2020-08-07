import PySimpleGUI as sg
from bolsa_letras import Bolsa


def crear_lyt(evento):
    if (evento == "menu") | (evento == "volver_menu"):
        layout = [
            [
                sg.Text(
                    "SCRABBLE",
                    size=(50, 1),
                    justification="center",
                    pad=(25, 25),
                    font=("Arial", 20),
                )
            ],
            [
                sg.Button(
                    "Nueva partida",
                    key="nueva_partida",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Cargar partida",
                    key="cargar",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Top 10",
                    key="top_ten",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Configuración",
                    key="config",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Salir",
                    key="salir",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
        ]

    elif (
        (evento == "config")
        | (evento == "volver_cfg_time")
        | (evento == "volver_cfg_fyc")
        | (evento == "volver_cfg")
    ):
        layout = [
            [
                sg.Text(
                    "Configuración",
                    size=(25, 1),
                    justification="center",
                    pad=(30, 30),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Button(
                    "Tiempo de partida",
                    key="tiempo_de_partida",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Letras",
                    key="letras",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Dificultad",
                    key="dificultad",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Tamaño del tablero",
                    key="tamaño_tablero",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 3),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_menu",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(20, 1),
                    pad=(15, 15),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "dificultad":
        layout = [
            [
                sg.Text(
                    "Dificultad",
                    size=(25, 1),
                    justification="center",
                    pad=(20, 20),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Button(
                    "Facil",
                    key="facil",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Medio",
                    key="medio",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Dificil",
                    key="dificil",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_cfg",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
        ]
    elif (
        (evento == "letras")
        | (evento == "volver_ltrs_val")
        | (evento == "volver_ltrs_cant")
    ):
        layout = [
            [
                sg.Text(
                    "Letras",
                    size=(30, 1),
                    justification="center",
                    pad=(50, 50),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Button(
                    "Cantidad de letras",
                    key="cantidad_letras",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Valores de letras",
                    key="puntos_por_letra",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_cfg",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "cantidad_letras":
        layout = [
            [
                sg.Text(
                    "Cantidad de letras",
                    size=(30, 1),
                    justification="center",
                    pad=(30, 30),
                    font=("Arial", 25),
                )
            ],
            [
                sg.Text("     A", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="A",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=11,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     B", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="B",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     C", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="C",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     D", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="D",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     E", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="E",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=11,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     F", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="F",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
            ],
            [
                sg.Text("     G", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="G",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     H", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="H",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     I", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="I",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=6,
                ),
            ],
            [
                sg.Text("     J", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="J",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     K", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="K",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     L", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="L",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     M", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="M",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     N", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="N",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=5,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Ñ", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Ñ",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     O", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="O",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=8,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     P", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="P",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Q", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Q",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     R", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="R",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     S", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="S",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=7,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     T", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="T",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     U", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="U",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     V", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="V",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=6,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     W", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="W",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     X", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="X",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Y", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Y",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Z", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Z",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
            ],
            [sg.Text("-" * 56, justification="c", font=("Helvetica", 15),)],
            [
                sg.Text("Total", size=(5, 1), justification="c", font=("Arial", 15),),
                sg.Text(
                    "99",
                    size=(4, 1),
                    key="cant_Total",
                    justification="c",
                    font=("Arial", 15),
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_ltrs_cant",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "puntos_por_letra":
        layout = [
            [
                sg.Text(
                    "Valores de letras",
                    size=(25, 1),
                    justification="center",
                    pad=(50, 50),
                    font=("Arial", 25),
                )
            ],
            [
                sg.Text("     A", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="A",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     B", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="B",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     C", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="C",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
            ],
            [
                sg.Text("     D", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="D",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     E", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="E",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     F", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="F",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     G", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="G",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     H", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="H",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     I", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="I",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     J", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="J",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=6,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     K", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="K",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=8,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     L", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="L",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     M", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="M",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     N", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="N",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Ñ", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Ñ",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=8,
                ),
            ],
            [
                sg.Text("     O", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="O",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     P", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="P",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Q", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Q",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=8,
                ),
            ],
            [
                sg.Text("     R", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="R",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     S", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="S",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     T", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="T",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     U", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="U",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     V", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="V",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     W", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="W",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=8,
                ),
            ],
            [
                sg.Text("     X", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="X",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=8,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Y", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Y",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Z", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="Z",
                    orientation="h",
                    enable_events=True,
                    size=(5, 10),
                    default_value=10,
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_ltrs_val",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "tiempo_de_partida":
        layout = [
            [
                sg.Text(
                    "Tiempo (min)",
                    size=(25, 1),
                    justification="center",
                    pad=(50, 15),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Slider(
                    range=(1, 60),
                    key="cant_tiempo",
                    orientation="h",
                    enable_events=True,
                    size=(50, 25),
                    pad=(0, 15),
                    default_value=30,
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_cfg_time",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "tamaño_tablero":
        layout = [
            [
                sg.Text(
                    "Tamaño del tablero",
                    size=(25, 1),
                    justification="center",
                    pad=(50, 15),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Text(
                    "Filas",
                    size=(25, 1),
                    justification="center",
                    pad=(50, 15),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Slider(
                    range=(6, 20),
                    key="cant_filas",
                    orientation="h",
                    enable_events=True,
                    size=(50, 25),
                    pad=(0, 15),
                    default_value=7,
                ),
            ],
            [
                sg.Text(
                    "Columnas",
                    size=(25, 1),
                    justification="center",
                    pad=(50, 15),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Slider(
                    range=(6, 20),
                    key="cant_columnas",
                    orientation="h",
                    enable_events=True,
                    size=(50, 25),
                    pad=(0, 15),
                    default_value=7,
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_cfg_fyc",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif (evento == "top_ten") | (evento == "volver_tops"):
        layout = [
            [
                sg.Text(
                    "TOP 10",
                    size=(30, 1),
                    justification="center",
                    pad=(20, 20),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Button(
                    "Fácil",
                    key="top_ten_facil",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Medio",
                    key="top_ten_medio",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Difícil",
                    key="top_ten_dificil",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "General",
                    key="top_ten_gen",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_menu",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "top_ten_facil":
        layout = [
            [
                sg.Text(
                    "TOP 10 - FACIL",
                    size=(30, 1),
                    justification="center",
                    pad=(50, 50),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Text(
                    "1°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "2°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "3°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "4°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "5°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "6°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "7°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "8°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "9°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "10°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_tops",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "top_ten_medio":
        layout = [
            [
                sg.Text(
                    "TOP 10 - MEDIO",
                    size=(30, 1),
                    justification="center",
                    pad=(50, 50),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Text(
                    "1°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "2°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "3°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "4°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "5°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "6°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "7°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "8°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "9°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "10°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_tops",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "top_ten_dificil":
        layout = [
            [
                sg.Text(
                    "TOP 10 - DIFICIL",
                    size=(30, 1),
                    justification="center",
                    pad=(50, 50),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Text(
                    "1°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "2°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "3°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "4°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "5°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "6°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "7°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "8°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "9°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "10°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_tops",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "top_ten_gen":
        layout = [
            [
                sg.Text(
                    "TOP 10 - GENERAL",
                    size=(30, 1),
                    justification="center",
                    pad=(50, 50),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Text(
                    "1°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "2°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "3°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "4°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "5°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "6°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "7°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "8°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "9°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Text(
                    "10°", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
                sg.Text(
                    "???", size=(15, 1), justification="center", font=("Arial", 15),
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_tops",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    return layout


def crear_partida(cfg):
    # (filas, columnas, dificultad, tiempo, cantidad_letras)
    layout = []
    # bolsa = Bolsa()
    # letras = bolsa.sacar_letras(7)
    dicc_puntos = {}
    if cfg["dificultad"] == "facil":
        for i in range(cfg["Filas"]):
            a = []
            for j in range(cfg["Columnas"]):
                if (i % 2 == cfg["Filas"] % 2) and (j % 2 == cfg["Filas"] % 2):
                    a.append(
                        sg.Button(
                            " ",
                            size=(2, 2),
                            key=(i, j),
                            pad=(1, 1),
                            button_color=("white", "green"),
                        )
                    )
                    dicc_puntos[(i, j)] = 2
                else:
                    if ((i % 2 == 0) & (j % 2 == 1)) or ((i % 2 == 1) & (j % 2 == 0)):
                        a.append(
                            sg.Button(
                                " ",
                                size=(2, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "blue"),
                            )
                        )
                        dicc_puntos[(i, j)] = 1.5
                    else:
                        a.append(
                            sg.Button(" ", size=(2, 2), key=(i, j), pad=(1, 1))
                        )
                        dicc_puntos[(i, j)] = 1
            layout.append(a)
    elif cfg["dificultad"] == "medio":
        for i in range(cfg["Filas"]):
            a = []
            for j in range(cfg["Columnas"]):
                if (
                    (i == 0 and j == 0)
                    or (i == cfg["Filas"] - 1 and j == cfg["Columnas"] - 1)
                    or (i == 0 and j == cfg["Columnas"] - 1)
                    or (i == cfg["Filas"] - 1 and j == 0)
                ):
                    a.append(
                        sg.Button(
                            " ",
                            size=(2, 2),
                            key=(i, j),
                            pad=(1, 1),
                            button_color=("white", "green"),
                        )
                    )
                    dicc_puntos[(i, j)] = 2
                else:
                    if (i % 2 == 0) & (j % 2 == 1):
                        a.append(
                            sg.Button(
                                " ",
                                size=(2, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "blue"),
                            )
                        )
                        dicc_puntos[(i, j)] = 1.5
                    elif (i % 2 == 1) & (j % 2 == 0):
                        a.append(
                            sg.Button(
                                " ",
                                size=(2, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "red"),
                            )
                        )
                        dicc_puntos[(i, j)] = 0.8
                    else:
                        a.append(
                            sg.Button(" ", size=(2, 2), key=(i, j), pad=(1, 1))
                        )
                        dicc_puntos[(i, j)] = 1
            layout.append(a)
    elif cfg["dificultad"] == "dificil":
        for i in range(cfg["Filas"]):
            a = []
            for j in range(cfg["Columnas"]):
                if (
                    (i == 0 and j == 0)
                    or (i == cfg["Filas"] - 1 and j == cfg["Columnas"] - 1)
                    or (i == 0 and j == cfg["Columnas"] - 1)
                    or (i == cfg["Filas"] - 1 and j == 0)
                ):
                    a.append(
                        sg.Button(
                            " ",
                            size=(2, 2),
                            key=(i, j),
                            pad=(1, 1),
                            button_color=("white", "purple"),
                        )
                    )
                    dicc_puntos[(i, j)] = 0.5
                else:
                    if (i % 2 == 0) & (j % 2 == 1):
                        a.append(
                            sg.Button(
                                " ",
                                size=(2, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "blue"),
                            )
                        )
                        dicc_puntos[(i, j)] = 1.5
                    elif (i % 2 == 1) & (j % 2 == 0):
                        a.append(
                            sg.Button(
                                " ",
                                size=(2, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "red"),
                            )
                        )
                        dicc_puntos[(i, j)] = 0.8
                    else:
                        a.append(
                            sg.Button(" ", size=(2, 2), key=(i, j), pad=(1, 1))
                        )
                        dicc_puntos[(i, j)] = 1
            layout.append(a)
    cfg["tablero"] = (dicc_puntos)
    a = []
    for j in range(7):
        a.append(
            sg.Button(
                # letras[j],
                size=(3, 3),
                key="letra" + str(j),
                button_color=("black", "lightblue"),
            )
        )

    b = []
    for j in range(7):
        b.append(sg.Button("*", size=(3, 3), key="letraM" + str(j), button_color=("white", "blue"),))

    layout.append(a)
    layout.insert(0, b)
    layout.append(
        [
            sg.Button(
                "Iniciar",
                key=("iniciar"),
                border_width=5,
                button_color=("white", "green"),
                size=(3, 3),
                font=("Helvetica", 12),
            ),
            sg.Button(
                "Finalizar turno",
                key=("fin-turno"),
                border_width=5,
                button_color=("white", "red"),
                size=(5, 3),
                font=("Helvetica", 12),
            ),
            sg.Button(
                "Deshacer",
                key=("vaciar"),
                border_width=5,
                button_color=("black", "pink"),
                size=(5, 3),
                pad=((1, 15), 15, 1),
                font=("Helvetica", 12),
            ),
            sg.Button(
                "Cambiar letras",
                key=("cambio"),
                border_width=5,
                button_color=('black', 'lightblue'),
                size=(5, 3),
                pad=((1, 15), 15, 1),
                font=("Helvetica", 12),
            ),
            sg.Button(
                "Guardar Partida",
                key=("guardar"),
                border_width=5,
                button_color=('black', 'lightblue'),
                size=(5, 3),
                pad=((1, 15), 15, 1),
                font=("Helvetica", 12),
            ),
            sg.Button(
                "Finalizar partida",
                key=("fin-partida"),
                border_width=5,
                button_color=('black', 'lightblue'),
                size=(5, 3),
                pad=((1, 15), 15, 1),
                font=("Helvetica", 12),
            ),
        ]
    )
    return layout
