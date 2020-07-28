import PySimpleGUI as sg


def crear_lyt(evento):
    if (evento == "menu") | (evento == "volver_menu"):
        layout = [
            [
                sg.Text(
                    "SCRABBLE",
                    size=(50, 1),
                    justification="center",
                    pad=(50, 35),
                    font=("Arial", 20),
                )
            ],
            [
                sg.Button(
                    "Nueva partida",
                    key="nueva_partida",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(35, 3),
                    pad=(30, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Cargar partida",
                    key="cargar",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(35, 3),
                    pad=(30, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Top 10",
                    key="top_ten",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(35, 3),
                    pad=(30, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Configuración",
                    key="config",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(35, 3),
                    pad=(30, 15),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Salir",
                    key="salir",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(35, 3),
                    pad=(30, 15),
                    font=("Arial", 12),
                )
            ],
        ]

    elif (evento == "config") | (evento == "volver_cfg"):
        layout = [
            [
                sg.Text(
                    "Configuración",
                    size=(25, 1),
                    justification="center",
                    pad=(50, 50),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Button(
                    "Tiempo de partida",
                    key="tiempo_de_partida",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Letras",
                    key="letras",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Dificultad",
                    key="dificultad",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(30, 3),
                    pad=(20, 20),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Tamaño del tablero",
                    key="tamaño_tablero",
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
                    size=(50, 3),
                    pad=(30, 30),
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
                    pad=(50, 50),
                    font=("Arial", 15),
                )
            ],
            [
                sg.Button(
                    "Facil",
                    key="facil",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Medio",
                    key="medio",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
            [
                sg.Button(
                    "Dificil",
                    key="dificil",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
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
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif (evento == "letras") | (evento == "volver_ltrs"):
        layout = [
            [
                sg.Text(
                    "Letras",
                    size=(25, 1),
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
                    size=(50, 3),
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
                    size=(50, 3),
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
                    size=(50, 3),
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
                    key="cant_A",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=11,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     B", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_B",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     C", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_C",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     D", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_D",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     E", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_E",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=11,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     F", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_F",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
            ],
            [
                sg.Text("     G", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_G",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     H", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_H",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     I", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_I",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=6,
                ),
            ],
            [
                sg.Text("     J", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_J",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     K", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_K",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     L", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_L",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     M", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_M",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     N", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_N",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=5,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Ñ", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_Ñ",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     O", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_O",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=8,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     P", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_P",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Q", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_Q",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     R", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_R",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     S", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_S",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=7,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     T", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_T",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     U", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_U",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     V", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_V",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=6,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     W", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_W",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     X", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_X",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Y", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_Y",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Z", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="cant_Z",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
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
                    key="volver_ltrs",
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
                    key="val_A",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     B", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_B",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     C", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_C",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
            ],
            [
                sg.Text("     D", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_D",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     E", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_E",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     F", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_F",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
            ],
            [
                sg.Text("     G", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_G",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=2,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     H", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_H",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     I", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_I",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     J", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_J",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=6,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     K", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_K",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=8,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     L", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_L",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     M", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_M",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     N", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_N",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Ñ", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_Ñ",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=8,
                ),
            ],
            [
                sg.Text("     O", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_O",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     P", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_P",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=3,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Q", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_Q",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=8,
                ),
            ],
            [
                sg.Text("     R", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_R",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     S", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_S",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     T", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_T",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
            ],
            [
                sg.Text("     U", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_U",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=1,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     V", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_V",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     W", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_W",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=8,
                ),
            ],
            [
                sg.Text("     X", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_X",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=8,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Y", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_Y",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=4,
                ),
                sg.VerticalSeparator(pad=None),
                sg.Text("     Z", size=(5, 1), justification="l", font=("Arial", 15),),
                sg.Slider(
                    range=(1, 20),
                    key="val_Z",
                    orientation="h",
                    enable_events=True,
                    size=(5, 20),
                    default_value=10,
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_ltrs",
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
                    size=(50, 25),
                    pad=(0, 15),
                    default_value=30,
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_cfg",
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
                    range=(1, 25),
                    key="cant_filas",
                    orientation="h",
                    size=(50, 25),
                    pad=(0, 15),
                    default_value=10,
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
                    range=(1, 25),
                    key="cant_columnas",
                    orientation="h",
                    size=(50, 25),
                    pad=(0, 15),
                    default_value=10,
                ),
            ],
            [
                sg.Button(
                    "Volver",
                    key="volver_cfg",
                    border_width=7,
                    button_color=("white", "lightblue"),
                    size=(50, 3),
                    pad=(30, 30),
                    font=("Arial", 12),
                )
            ],
        ]
    elif evento == "top_ten":
        None
    return layout


def crear_partida(Filas, Columnas, dificultad, tiempo, cantidad_letras):
    # (filas, columnas, dificultad, tiempo, cantidad_letras)
    layout = []
    if dificultad == "facil":
        for i in range(Filas):
            a = []
            for j in range(Columnas):
                if (i % 2 == Filas % 2) and (j % 2 == Columnas % 2):
                    a.append(
                        sg.Button(
                            " ",
                            size=(2, 2),
                            key=(i, j),
                            pad=(1, 1),
                            button_color=("white", "green"),
                        )
                    )
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
                    else:
                        a.append(sg.Button(" ", size=(2, 2), key=(i, j), pad=(1, 1)))
            layout.append(a)
    elif dificultad == "medio":
        for i in range(Filas):
            a = []
            for j in range(Columnas):
                if (
                    (i == 0 and j == 0)
                    or (i == Filas - 1 and j == Columnas - 1)
                    or (i == 0 and j == Columnas - 1)
                    or (i == Filas - 1 and j == 0)
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
                    else:
                        a.append(sg.Button(" ", size=(2, 2), key=(i, j), pad=(1, 1)))
            layout.append(a)
    elif dificultad == "dificil":
        for i in range(Filas):
            a = []
            for j in range(Columnas):
                if (
                    (i == 0 and j == 0)
                    or (i == Filas - 1 and j == Columnas - 1)
                    or (i == 0 and j == Columnas - 1)
                    or (i == Filas - 1 and j == 0)
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
                    else:
                        a.append(sg.Button(" ", size=(2, 2), key=(i, j), pad=(1, 1)))
            layout.append(a)

    a = []
    for j in range(7):
        a.append(
            sg.Button(
                # letras[j],
                size=(3, 3),
                key=("letra" + str(j)),
                button_color=("black", "lightblue"),
            )
        )

    b = []
    for j in range(7):
        b.append(sg.Button(size=(3, 3), button_color=("white", "blue"),))

    layout.append(a)
    layout.insert(0, b)

    return layout
