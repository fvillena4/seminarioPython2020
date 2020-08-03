import PySimpleGUI as sg
import crear_layout as crear
import Scrabble

# import Trabajo_Final.py as play

window = sg.Window(
    "Menú",
    crear.crear_lyt("menu"),
    resizable=True,
    element_justification="c",
    background_color="#143430",
)


def switch(ky):
    aux = [
        "cant_A",
        "cant_B",
        "cant_C",
        "cant_D",
        "cant_E",
        "cant_F",
        "cant_G",
        "cant_H",
        "cant_I",
        "cant_J",
        "cant_K",
        "cant_L",
        "cant_M",
        "cant_N",
        "cant_Ñ",
        "cant_O",
        "cant_P",
        "cant_Q",
        "cant_R",
        "cant_S",
        "cant_T",
        "cant_U",
        "cant_V",
        "cant_W",
        "cant_X",
        "cant_Y",
        "cant_Z",
    ]
    if ky in aux:
        return True
    else:
        return False


def switch2(evento):
    aux = [
        "config",
        "tiempo_de_partida",
        "cantidad_letras",
        "puntos_por_letra",
        "letras",
        "dificultad",
        "tamaño_tablero",
        "volver_menu",
        "volver_ltrs",
        "top_ten",
        "volver_tops",
        "top_ten_gen",
        "top_ten_facil",
        "top_ten_medio",
        "top_ten_dificil",
        "volver_cfg",
    ]  #  "cargar"
    if evento in aux:
        return True
    else:
        return False


config = {
    "Filas": 10,
    "Columnas": 10,
    "dificultad": "facil",
    "tiempo": 30,
    "cant_letras": {
        "cant_A": 11.0,
        "cant_B": 3.0,
        "cant_C": 4.0,
        "cant_D": 4.0,
        "cant_E": 11.0,
        "cant_F": 2.0,
        "cant_G": 2.0,
        "cant_H": 2.0,
        "cant_I": 6.0,
        "cant_J": 2.0,
        "cant_K": 1.0,
        "cant_L": 4.0,
        "cant_M": 3.0,
        "cant_N": 5.0,
        "cant_Ñ": 1.0,
        "cant_O": 8.0,
        "cant_P": 2.0,
        "cant_Q": 1.0,
        "cant_R": 4.0,
        "cant_S": 7.0,
        "cant_T": 4.0,
        "cant_U": 2.0,
        "cant_V": 6.0,
        "cant_W": 1.0,
        "cant_X": 1.0,
        "cant_Y": 1.0,
        "cant_Z": 1.0,
    },
    "valores_letras": {
        "val_A": 1.0,
        "val_B": 3.0,
        "val_C": 2.0,
        "val_D": 2.0,
        "val_E": 1.0,
        "val_F": 4.0,
        "val_G": 2.0,
        "val_H": 4.0,
        "val_I": 1.0,
        "val_J": 6.0,
        "val_K": 8.0,
        "val_L": 1.0,
        "val_M": 3.0,
        "val_N": 1.0,
        "val_Ñ": 8.0,
        "val_O": 1.0,
        "val_P": 3.0,
        "val_Q": 8.0,
        "val_R": 1.0,
        "val_S": 1.0,
        "val_T": 1.0,
        "val_U": 1.0,
        "val_V": 4.0,
        "val_W": 8.0,
        "val_X": 8.0,
        "val_Y": 4.0,
        "val_Z": 10.0,
    },
}


while True:
    event, values = window.Read()
    print(event, values)

    if (event == None) | (event == "salir"):
        break
    # Guardando configuración
    elif event == "volver_cfg_time":
        config["tiempo"] = int(values["cant_tiempo"])
        window.close()
        window = sg.Window(
            "Menú",
            crear.crear_lyt(event),
            finalize=True,
            resizable=True,
            element_justification="c",
            background_color="#143430",
        )
    elif (event == "facil") | (event == "medio") | (event == "dificil"):
        config["dificultad"] = str(event)
    elif event == "volver_cfg_fyc":
        config["Filas"] = int(values["cant_filas"])
        config["Columnas"] = int(values["cant_columnas"])
        window.close()
        window = sg.Window(
            "Menú",
            crear.crear_lyt(event),
            finalize=True,
            resizable=True,
            element_justification="c",
            background_color="#143430",
        )
    elif event == "volver_ltrs_val":
        config["valores_letras"] = values
        window.close()
        window = sg.Window(
            "Menú",
            crear.crear_lyt(event),
            finalize=True,
            resizable=True,
            element_justification="c",
            background_color="#143430",
        )
    elif event == "volver_ltrs_cant":
        if int(sum(values.values())) > (config["Filas"] * config["Columnas"]):
            sg.popup(
                "La cantidad total de letras ("
                + str(int(sum(values.values())))
                + ") supera al tamaño del tablero ("
                + str((config["Filas"] * config["Columnas"]))
                + " casilleros)"
            )
        else:
            config["cant_letras"] = values
            window.close()
            window = sg.Window(
                "Menú",
                crear.crear_lyt(event),
                finalize=True,
                resizable=True,
                element_justification="c",
                background_color="#143430",
            )
    elif event == "nueva_partida":  # Iniciar una nueva partida
        window.close()
        layout = crear.crear_partida(config)
        # window = sg.Window(
        #     "SCRABBLE",
        #     crear.crear_partida(config),
        #     finalize=True,
        #     resizable=True,
        #     element_justification="c",
        #     background_color="#143430",
        # )
        Scrabble
    elif switch2(
        event
    ):  # llama al constructor de layouts si encuentra el evento en el switch2
        window.close()
        window = sg.Window(
            "Menú",
            crear.crear_lyt(event),
            finalize=True,
            resizable=True,
            element_justification="c",
            background_color="#143430",
        )
    elif event == "cargar":  # Iniciar una partida guardada
        None
    elif switch(event):
        window.Element("cant_Total").Update(str(int(sum(values.values()))))
