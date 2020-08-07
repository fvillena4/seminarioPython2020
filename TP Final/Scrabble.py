"""Este modulo realiza el juego principal, que se llama desde el menu."""

import pattern.es as pt
import PySimpleGUI as sg
import random
from bolsa_letras import Bolsa
from jugador import Jugador
from juez import Juez
import crear_layout as crear
import json
from maquina import Maquina


def jugar_partida(config, partida={}):
    """Juega la partida tanto la nueva partica como una cargada."""

    def iniciar(nombre):
        """Elige aleatoriamente para comenzar entre el jugador y la maquina."""
        x = random.randint(0, 1)
        if x == 0:
            sg.popup_ok("Comienza el jugador: " + nombre)
            return True, nombre
        else:
            sg.popup_ok("Comienza a jugar la maquina")
            return True, "maquina"

    def abrir_partida(partida, window):
        """Usa los componentes de la partida guardada."""
        try:
            tablero = partida["tablero"]
            for i in tablero.keys():
                window[i].Update(tablero[i])
            un_jugador = list(partida["puntos_jugador"].keys())[0]
            bolsa = Bolsa(un_ABC=partida["letras_bolsa"])
            guido = Maquina(unas_letras=partida["letras_M"], un_nivel=partida["dificultad"], filas=partida["filas"], columnas=partida["columnas"])
            jugador = Jugador(un_jugador, partida["letras_J"], partida["dificultad"], partida["filas"], partida["columnas"])
            juez = Juez(partida["dificultad"], partida["tabla_puntajes"], config["tablero"], un_jugador, partida["turno"])
            letras_j = partida["letras_J"]
            for clave, valor in letras_j.items():
                window[clave].Update(valor)
            return True, guido, jugador, juez
        except FileNotFoundError or KeyError:
            sg.Popup("Ha ocurrido un error abriendo la partida.")
            return False, [], [], []

    def guardar_partida():
        try:
            with open('partida.json', 'w') as file:
                partida = {}
                tablero = config["tablero"]
                multiplicador = config["tablero"]
                coordenadas = list(map(str, multiplicador.keys()))
                valores = multiplicador.values()
                multiplicador = dict(zip(coordenadas, valores))
                for i in list(tablero.keys()):
                    tablero[i] = window[i].GetText()
                coordenadas = list(map(str, tablero.keys()))
                valores = tablero.values()
                tablero = dict(zip(coordenadas, valores))
                partida["tablero"] = tablero
                partida["turno"] = juez.turno
                partida["letras_M"] = guido.letras
                partida["letras_J"] = jugador.letras
                partida["tabla_puntajes"] = juez.tabla_puntaje
                partida["multiplicadores"] = multiplicador
                partida["puntos_jugador"] = juez.jugadores
                partida["letras_bolsa"] = bolsa.ABC
                partida["dificultad"] = config["dificultad"]
                partida["filas"] = config["Filas"]
                partida["columnas"] = config["Columnas"]
                partida["tiempo"] = config["tiempo"]
                json.dump(partida, file)
                return True
        except FileNotFoundError or KeyError:
            sg.Popup("Ha ocurrido un error.")
            return False

    w, h = sg.Window.get_screen_size()
    window = sg.Window(
        "SCRABBLE",
        crear.crear_partida(config),
        finalize=True,
        size=(w, h),
        resizable=True,
        element_justification="c",
        background_color="#143430",
    )
    window.Maximize()
    bolsa = Bolsa(un_ABC=config["cant_letras"])
    letras_jugador = bolsa.sacar_letras(7)
    letras_maquina = bolsa.sacar_letras(7)
    # window.Maximize()
    claves = []
    for j in range(7):
        clave = "letra" + str(j)
        window[clave].Update(letras_jugador[j])
        claves.append(clave)
    mis_letras = dict(zip(claves, letras_jugador))
    comenzo = False
    final = False
    abri = False
    while not final:
        if partida:
            abri, guido, jugador, juez = abrir_partida(partida, window)
            comenzo = abri
        event, values = window.Read()
        if event == None or event == "fin-partida":
            valor = sg.popup_yes_no("¿Desea guardar la partida?")
            if valor == "Yes":
                if comenzo:
                    guardado = guardar_partida()
                    if guardado:
                        sg.Popup("La partida se ha guardado exitosamente. Saliendo del juego")
                        break
                    else:
                        sg.Popup("No se ha podido guardar la partida.")
                else:
                    sg.Popup("El juego aun no ha comenzado.")
            final = True
            break
        elif event == "Referencias":
            window2 = sg.Window(
                "Referencias",
                crear.crear_lyt(event),
                finalize=True,
                resizable=True,
                element_justification="c",
                background_color="#143430",
            )
            event, values = window2.Read()
            while not (event == None or event == "cerrar_referencias"):
                None
            window2.close()
        elif event == "guardar":
            if comenzo:
                guardado = guardar_partida()
                if guardado:
                    sg.Popup("La partida se ha guardado exitosamente. Saliendo del juego")
                    break
                    final = True
                else:
                    sg.Popup("No se ha podido guardar la partida.")
            else:
                sg.Popup("El juego aun no ha comenzado.")
        elif event == "iniciar" and not comenzo:
            nombre = sg.popup_get_text("Ingrese su nombre: ")
            window["nombre_player"].update(nombre + ": ")
            comenzo, primero = iniciar(nombre)
            guido = Maquina(unas_letras=letras_maquina, un_nivel=config["dificultad"], filas=config["Filas"], columnas=config["Columnas"])
            jugador = Jugador(nombre, mis_letras, config["dificultad"], config["Filas"], config["Columnas"])
            juez = Juez(config["dificultad"], config['valores_letras'], config["tablero"], nombre, primero)
        elif not comenzo:
            sg.popup_ok("Para comenzar oprima el boton iniciar")
        if comenzo and not final:
            if abri:
                sg.Popup("Ahora es el turno de "+str(juez.turno))
                nombre = jugador.nombre
            if(juez.turno == nombre):
                jugador.jugar(window, juez, bolsa)
                agregue = jugador._agregar_letras(window, bolsa)
                if not agregue:
                    sg.Popup("No se pudo agregar letras.")
                    sg.Popup("Termino la partida, porque no hay mas letras.")
                    final = True
                else:
                    window["puntaje_player"].update(juez.jugadores[nombre])
            elif(juez.turno == "maquina"):
                jugue, motivo = guido._jugar(window, juez, config)
                if not jugue:
                    if motivo == "no hay espacios":
                        final = True
                        sg.Popup("Termino la partida por la maquina no encontro espacio.")
                    elif motivo == "no hay palabras validas":
                        juez.turno = nombre
                        sg.Popup("La maquina no pudo formar palabras")
                else:
                    guido.agregar_letras(bolsa.sacar_letras(7-len(guido.letras)))
                    juez.turno = nombre
                    window["puntaje_maquina"].update(juez.jugadores["maquina"])
                    sg.Popup("Es el turno de: "+str(nombre))
    if comenzo:
        podio = juez._determinar_ganador()
        if 0 in podio.keys():
            sg.Popup("Hubo un empate con: "+str(podio[0][0][1])+" puntos.")
        else:
            sg.Popup("El ganador es: "+str(podio[1][0])+" con "+str(podio[1][1])+" puntos.")
    window.Close()
