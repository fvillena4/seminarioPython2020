

import PySimpleGUI as sg

from bolsa_letras import Bolsa

from juez import Juez


class Jugador():
    """Representa al jugador que va a jugar contra la maquina."""

    nombre = str()
    _nivel = str()
    _letras = dict()  # claves=posicion del atril y valores=letras

    def __init__(self, un_nombre, unas_letras, un_nivel, filas, columnas):
        """Inicializa (Constructor) de la clase."""
        self.nombre = un_nombre
        self._nivel = un_nivel
        self._letras = unas_letras
        # self._filas = filas
        # self._columnas = columnas
        self._cant_cambios = 0

    @property
    def letras(self):
        return self._letras

    @property
    def cant_cambios(self):
        return self._cant_cambios

    def _agregar_letras(self, window, bolsa):
        pos_letras = []
        for i in self._letras.keys():
            if window[i].GetText() == " ":
                pos_letras.append(i)
        letras_nuevas = bolsa.sacar_letras(len(pos_letras))
        if len(letras_nuevas) == len(pos_letras):
            for i in range(len(pos_letras)):
                self._letras[pos_letras[i]] = letras_nuevas[i]
                window[pos_letras[i]].Update(letras_nuevas[i])
                window[pos_letras[i]].Update(button_color=('black', 'lightblue'))
            return True
        elif len(letras_nuevas) < len(pos_letras):
            sg.Popup("La cantidad de letras nuevas es menor a la cantidad de posiciones a cubrir.")
            return False

    def sigue(self, posiciones, nueva_pos):
        "Verifica que siga en horizontal o vertical pero no las dos a la vez."
        if posiciones:  # si hay elementos en la lista de posiciones
            ult = posiciones[len(posiciones)-1]  # agarro al ultimo de la lista
            if (ult[0]+1 == nueva_pos[0] and ult[1] == nueva_pos[1]) or (ult[0] == nueva_pos[0] and ult[1]+1 == nueva_pos[1]):  # si sigue en la misma columna y avanza por fila
                if len(posiciones) >= 2:
                    ante_ult = posiciones[len(posiciones)-2]
                    if (ante_ult[0]+1 == nueva_pos[0] and ante_ult[1]+1 == nueva_pos[1]) or (ante_ult[0]+1 == nueva_pos[0] and ante_ult[1]+1 == nueva_pos[1]):
                        return False
                return True
            else:
                return False
        else:  # si la lista esta vacia
            return True

    def resetear(self, posiciones, window):
        """Deshace todo los movimientos que hice en el turno."""
        if posiciones:
            for i in posiciones:  # recorro las posiciones en las que agregue letras
                window[i].Update(disabled=False)  # las habilito
                window.FindElement(i).Update(" ")  # las actualizo para que esten vacias
            window.Refresh()
            for k in self._letras.keys():  # recorro las letras
                window[k].Update(disabled=False)  # las habilito
                window[k].Update(self._letras[k])  # devuelvo cada letra a su lugar
                window[k].Update(button_color=('black', 'lightblue'))
            window.Refresh()
        return [], []  # devuelvo listas vacias para las palabras y posiciones

    def cambiar_letras(self, window, bolsa, juez):
        """Cambia las letras del jugador.

        Permite elegir la cantidad de letras a cambiar.
        """
        letras_cambiar = {}  # creo un diccionario vacio; claves=posiciones de las letras y valores=letras a cambiar
        window[("vaciar")].set_size((9, 3))
        window[("vaciar")].Update("Deshacer cambio de letras.")
        window[("cambio")].set_size((9, 3))
        window[("cambio")].Update("Cambiar "+str(len(letras_cambiar))+" letras.")
        fin = False
        sg.Popup("Ingrese las letras que quiere cambiar.",
                 "Cuando finalize oprima Cambiar letras nuevamente.",
                 "Para salir oprima Deshacer cambio de letras.")
        while not fin:  # mientras que no cambie las letras
            event, values = window.Read()  # leo el evento y valor
            if event == None or event == "fin-partida":
                fin = True
                break
            letra = window.FindElement(event).GetText()  # obtengo el texto del evento
            if event in self._letras.keys() and letra in self._letras.values():  # si esta dentro de mis letras
                if len(letras_cambiar) < 7 and event not in letras_cambiar.keys():  # si la cantidad de letras a cambiar es menor que 7 y no elegi esa letra para cambiar(evitar cambiar varias veces la misma letra)
                    letras_cambiar[event] = letra  # actualizo el diccionario de las letras a cambiar
                    window[event].Update(button_color=('red', 'lightblue'))  # cambio el color para que el usuario note que letras ya eligio
                    sg.popup("Las letras a cambiar son: "+str(list(letras_cambiar.values())))  # informo que letras by a cambiar
                    window[("cambio")].Update("Cambiar "+str(len(letras_cambiar))+" letras.")  # actualizo el boton de cambiar
                elif not len(letras_cambiar) < 7:  # si quiero cambiar mas de la cantidad de mis letras
                    sg.popup("No puede cambiar mas de la cantidad de sus letras.")
                elif event in letras_cambiar.keys():  #  si la posicion de la letra ya se encuentra
                    sg.popup("No puede cambiar la misma letra 2 veces")
            elif event == "cambio":  # si quiero cambiar
                if len(letras_cambiar) > 0:  # si tengo alguna letra que cambiar
                    letras_viejas = list(letras_cambiar.values())  # uso una variable auxiliar para las letras viejas
                    pos_letras = list(letras_cambiar.keys())  # uso una variable auxiliar para las posiciones
                    letras_nuevas = bolsa.sacar_letras(len(letras_viejas))  # saco de la bolsa la cantidad de letras que quiero cambiar
                    if len(letras_nuevas) == len(letras_cambiar):  # si la cantidad de letras nuevas es igual a la cantidad de letras viejas
                        for i in range(len(pos_letras)):  # recorro las posiciones
                            window[pos_letras[i]].Update(letras_nuevas[i])  # actualizo las posiciones con las letras nuevas
                            window[pos_letras[i]].Update(button_color=('black', 'lightblue'))
                        self._letras.update(dict(zip(pos_letras, letras_nuevas)))  # actualizo las letras del jugador
                        window[("vaciar")].set_size((5, 3))
                        window[("vaciar")].Update("Deshacer")
                        window[("cambio")].set_size((5, 3))
                        window[("cambio")].Update("Cambiar letras")
                        fin = True  # termino
                        juez.turno = "maquina"
                        sg.Popup("Es el turno de: la maquina, porque cambiaste las letras")
                        self._cant_cambios += 1
                    elif len(letras_nuevas) < len(letras_viejas):
                        return True
                        sg.Popup("No hay suficientes letras en la bolsa.")
                else:
                    sg.popup("No eligio letras a cambiar")
            elif event == "vaciar":
                pos_letras = list(letras_cambiar.keys())  # uso una variable auxiliar para las posiciones
                for i in pos_letras:
                    window[i].Update(button_color=('black', 'lightblue'))
                window[("vaciar")].set_size((5, 3))
                window[("vaciar")].Update("Deshacer")
                window[("cambio")].set_size((5, 3))
                window[("cambio")].Update("Cambiar letras")
                fin = True  # termino
            elif not(event in self._letras.keys() and letra in self._letras.values()):
                sg.popup("Esa no es una letra valida.")

    def _verificar_juez(self, palabra, juez):
        """Se comunica con el juez para validar la palabra."""
        palabra = "".join(palabra).lower()  # junto las letras en su orden
        if juez._validar(palabra):  # si el juez me dice que es correcta
            sg.popup("La palabra: "+palabra+" es correcta")  # Le confirmo al jugador
            return True
        else:
            sg.popup("La palabra: "+palabra+" no existe. Ingrese otra palabra")  # Le aviso que la palabra no existe
            return False


    def jugar(self, window, juez, bolsa):
        fin = False  # representa si termine el turno
        palabra = []  # incializo una lista vacia donde van las letras que formaran la palabra
        posiciones = []  # incializo una lista vacia donde van las posiciones de las letras que agregue
        while not fin:  # mientras no haya terminado
            event, values = window.Read()  # leo event, values
            if event == None or event == "fin-partida":  # si el evento es salir
                fin = True
                break  # rompo el ciclo
            letra = window.FindElement(event).GetText()  # obtengo el texto del evento
            event_letra = event  # guardo el evento de la letra que tome
            if event_letra in self._letras.keys() and letra in self._letras.values():  # si esta en mis letras
                window[event_letra].Update(button_color=('white', 'lightblue'))
                event, values = window.Read()  # leo un lugar donde voy a poner la letra
                if event == None or event == "fin-partida":
                    fin = True
                    break
                if(window.FindElement(event).GetText() == " ") and (event not in self._letras.keys() and self.sigue(posiciones, event)):  # si esta vacio y no es el espacio de una letra y sigue(col o fila)
                    window.FindElement(event).Update(letra)  # pongo la letra en el casillero vacio
                    palabra.append(letra)  # agrego la letra a palabra
                    posiciones.append(event)  # agrego la posicion donde la agregamos
                    window[event].Update(disabled=True)  # actualizo la posicion donde la agregue para que no se pueda volver a modificar
                    window.FindElement(event_letra).Update(" ")  # actualizo para remplazar mi letra por un " "
                elif (event in self._letras.keys()):  # si el espacio seleccionado es un casillero de letra
                    sg.popup("Ese es un espacio de letra.Elija otro espacio.")
                elif (not self.sigue(posiciones, event)):  # si no sigue ni vertical ni horizontal
                    sg.popup("La palabra debe ingresarse ordenada.(Horizontal o Vertical)")
                else:  # si es un espacio ocupado
                    sg.popup("Ese es un espacio ocupado.Elija otro espacio.")
                window[event_letra].Update(button_color=('white', 'lightblue'))
            elif event == "vaciar":  # si me equivoque y quiero que me devuelva todas las letras
                palabra, posiciones = self.resetear(posiciones, window)
            elif event == "cambio":  # si quiero cambiar las letras
                if self._cant_cambios < 3:
                    self.cambiar_letras(window, bolsa, juez)
                else:
                    sg.Popup("Ya uso los 3 cambios de letras permitidos.")
            elif event == "fin-turno":  # si quiero terminar el turno
                if len(palabra) >= 2:  # si la palabra tiene 2 o mas letras
                    if self._verificar_juez(palabra, juez):  # la verifico con el juez
                        fin = True  # termine mi turno
                        puntos = juez._calcular_puntaje(palabra, posiciones, self.nombre)
                        palabra = []
                        posiciones = []
                        juez.turno = "maquina"  # le doy el turno a la maquina
                        sg.Popup("Es el turno de: la maquina.")
                    else:  # si no es una palabra valida
                        palabra, posiciones = self.resetear(posiciones, window)  # devuelvo las letras usadas
                else:
                    sg.popup("La palabra debe contener al menos 2 letras")
