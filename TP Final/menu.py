import PySimpleGUI as sg
import crear_layout as crear

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
        "val_A",
        "val_B",
        "val_C",
        "val_D",
        "val_E",
        "val_F",
        "val_G",
        "val_H",
        "val_I",
        "val_J",
        "val_K",
        "val_L",
        "val_M",
        "val_N",
        "val_Ñ",
        "val_O",
        "val_P",
        "val_Q",
        "val_R",
        "val_S",
        "val_T",
        "val_U",
        "val_V",
        "val_W",
        "val_X",
        "val_Y",
        "val_Z",
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
        "volver_cfg",
        "volver_ltrs",
    ]  # "top_ten", "cargar"
    if evento in aux:
        return True
    else:
        return False


while True:
    event, values = window.Read()
    print(event, values)

    if (event == None) | (event == "salir"):
        break
    elif event == "nueva_partida":  # Iniciar una nueva partida
        window.close()
        window = sg.Window(
            "Menú",
            crear.crear_partida(10, 10, "dificil", 20, 23),
            finalize=True,
            resizable=True,
            element_justification="c",
            background_color="#143430",
        )
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
    elif event == "top_ten":
        None
    elif switch(event):
        window.Element("cant_Total").Update(str(int(sum(values.values()))))
