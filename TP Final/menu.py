import PySimpleGUI as sg
import crear_layout as crear
import Scrabble
from pathlib import Path
import json

# import Trabajo_Final.py as play
config = {
    "tablero": {},
    "Filas": 7,
    "Columnas": 7,
    "dificultad": "facil",
    "tiempo": 30,
    "cant_letras": {
        "A": 11.0,
        "B": 3.0,
        "C": 4.0,
        "D": 4.0,
        "E": 11.0,
        "F": 2.0,
        "G": 2.0,
        "H": 2.0,
        "I": 6.0,
        "J": 2.0,
        "K": 1.0,
        "L": 4.0,
        "M": 3.0,
        "N": 5.0,
        "Ñ": 1.0,
        "O": 8.0,
        "P": 2.0,
        "Q": 1.0,
        "R": 4.0,
        "S": 7.0,
        "T": 4.0,
        "U": 2.0,
        "V": 6.0,
        "W": 1.0,
        "X": 1.0,
        "Y": 1.0,
        "Z": 1.0,
    },
    "valores_letras": {
        "A": 1.0,
        "B": 3.0,
        "C": 2.0,
        "D": 2.0,
        "E": 1.0,
        "F": 4.0,
        "G": 2.0,
        "H": 4.0,
        "I": 1.0,
        "J": 6.0,
        "K": 8.0,
        "L": 1.0,
        "M": 3.0,
        "N": 1.0,
        "Ñ": 8.0,
        "O": 1.0,
        "P": 3.0,
        "Q": 8.0,
        "R": 1.0,
        "S": 1.0,
        "T": 1.0,
        "U": 1.0,
        "V": 4.0,
        "W": 8.0,
        "X": 8.0,
        "Y": 4.0,
        "Z": 10.0,
    },
}
dicc_puntos = {}
for i in range(config["Filas"]):
    a = []
    for j in range(config["Columnas"]):
        if (i % 2 == config["Filas"] % 2) and (j % 2 == config["Filas"] % 2):
            dicc_puntos[(i, j)] = 2
        else:
            if ((i % 2 == 0) & (j % 2 == 1)) or ((i % 2 == 1) & (j % 2 == 0)):
                dicc_puntos[(i, j)] = 1.5
            else:
                dicc_puntos[(i, j)] = 1
config["tablero"].update(dicc_puntos)
window = sg.Window(
    "Menú",
    crear.crear_lyt("menu"),
    resizable=True,
    element_justification="c",
    background_color="#143430",
)


def switch(ky):
    aux = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "Ñ",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
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
        "volver_cfg",
    ]  #  "cargar"
    if evento in aux:
        return True
    else:
        return False


while True:
    event, values = window.Read()
    if (event == None) | (event == "salir"):
        break
    # Guardando configuración
    elif event == "volver_cfg_time":
        config["tiempo"] = int(values["cant_tiempo"])
        sg.Popup("El tiempo de partida sera "+str(config["tiempo"])+" minutos ")
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
        sg.Popup("Eligio el nivel: "+str(config["dificultad"]))
    elif event == "volver_cfg_fyc":
        config["Filas"] = int(values["cant_filas"])
        config["Columnas"] = int(values["cant_columnas"])
        sg.Popup("Eligio "+str(config["Filas"])+" filas y "+str(config["Columnas"])+" columnas.")
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
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                coordenadas = list(map(tuple, config["tablero"].keys()))
                valores = config["tablero"].values()
                config["tablero"] = dict(zip(coordenadas, valores))
        except FileNotFoundError:
            pass
        # print(config)
        layout = crear.crear_partida(config)
        Scrabble.jugar_partida(config)
    elif switch2(event):
        #  llama al constructor de layouts si encuentra el evento en el switch2
        window.close()
        window = sg.Window(
            "Menú",
            crear.crear_lyt(event),
            finalize=True,
            resizable=True,
            element_justification="c",
            background_color="#143430",
        )
        if event == "top_ten":
            try:
                with open('mejores.json', 'r') as file:
                    top = json.load(file)
                    top = dict(top)
                    for i in top.keys():
                        clave = str(i)
                        valor = top[i]
                        window[str("nombre"+clave)].Update(valor[0])
                        window[str("puntaje"+clave)].Update(valor[1])
                        window[str("dificultad"+clave)].Update(valor[2])
            except FileNotFoundError or KeyError:
                sg.Popup("Ha ocurrido un error en la carga del top 10.")
    elif event == "cargar":  # Iniciar una partida guardada
        window.close()
        try:
            with open('partida.json', 'r') as file:
                partida = json.load(file)
                coordenadas = list(map(eval, list(partida["tablero"].keys())))
                valores = partida["tablero"].values()
                partida["tablero"] = dict(zip(coordenadas, valores))
                coordenadas = list(map(eval, list(partida["multiplicadores"].keys())))
                valores = partida["tablero"].values()
                partida["multiplicadores"] = dict(zip(coordenadas, valores))
                config["tablero"] = partida["multiplicadores"]
                config["Filas"] = partida["filas"]
                config["Columnas"] = partida["columnas"]
                config["dificultad"] = partida["dificultad"]
                config["tiempo"] = partida["tiempo"]
                config["cant_letras"] = partida["letras_bolsa"]
                config["valores_letras"] = partida["tabla_puntajes"]
                layout = crear.crear_partida(config)
                Scrabble.jugar_partida(config, partida)
        except FileNotFoundError or KeyError:
            sg.Popup("Ha ocurrido un error en la carga de la partida.")
    elif switch(event):
        window.Element("cant_Total").Update(str(int(sum(values.values()))))
    print(config)
    with open('config.json', 'w') as file:
        coordenadas = list(map(str, config["tablero"].keys()))
        valores = config["tablero"].values()
        config["tablero"] = dict(zip(coordenadas, valores))
        json.dump(config, file)
    # except:
    #     sg.Popup("No se pudo crear el archivo")
