

import PySimpleGUI as sg

from bolsa_letras import Bolsa

from juez import Juez


class Jugador():
    """Representa al jugador que va a jugar contra la maquina."""

    nombre = str()
    _nivel = str()
    _letras = dict()  # claves=posicion del atril y valores=letras

    def __init__(self, un_nombre, unas_letras, un_nivel="facil"):
        """Inicializa (Constructor) de la clase."""
        self.nombre = un_nombre
        self._nivel = un_nivel
        self._letras = unas_letras

    def _agregar_letras(self, nuevas_letras):
        self._letras.extend(nuevas_letras)

    def sigue(self, posiciones, nueva_pos):
        "Verifica que siga en horizontal o vertical pero no las dos a la vez."
        if posiciones:  # si hay elementos en la lista de posiciones
            ult = posiciones[len(posiciones)-1]  # agarro al ultimo de la lista
            if ult[0][0]+1 == nueva_pos[0] and ult[0][1] == nueva_pos[1]:  # si sigue en la misma columna y avanza por fila
                return True
            elif ult[0][0] == nueva_pos[0] and ult[0][1]+1 == nueva_pos[1]:  # si sigue en la misma fila y avanza por columna
                return True
            else:
                return False
        else:  # si la lista esta vacia
            return True

    def resetear(self, posiciones, window):
        """Deshace todo los movimientos que hice en el turno."""
        print(posiciones)
        for i in posiciones:  # recorro las posiciones en las que agregue letras
            window[i].Update(disabled=False)  # las habilito
            window.FindElement(i).Update(" ")  # las actualizo para que esten vacias
        window.Refresh()
        for k in self._letras.keys():  # recorro las letras
            window[k].Update(disabled=False)  # las habilito
            window[k].Update(self._letras[k])  # devuelvo cada letra a su lugar
        window.Refresh()
        return [], []  # devuelvo listas vacias para las palabras y posiciones

    def cambiar_letras(self, window, bolsa):
        """Cambia las letras del jugador.

        Permite elegir la cantidad de letras a cambiar.
        """
        letras_cambiar = {}  # creo un diccionario vacio; claves=posiciones de las letras y valores=letras a cambiar
        window[("vaciar"), ].set_size((9, 3))
        window[("vaciar"), ].Update("Deshacer cambio de letras.")
        window[("cambio"), ].set_size((9, 3))
        window[("cambio"), ].Update("Cambiar "+str(len(letras_cambiar))+" letras.")
        fin = False
        sg.Popup("Ingrese las letras que quiere cambiar.",
                 "Cuando finalize oprima Cambiar letras nuevamente.",
                 "Para salir oprima Deshacer cambio de letras.")
        while not fin:  # mientras que no cambie las letras
            event, values = window.Read()  # leo el evento y valor
            if event == None:
                break
            letra = window.FindElement(event).GetText()  # obtengo el texto del evento
            if event in self._letras.keys() and letra in self._letras.values():  # si esta dentro de mis letras
                print(event in letras_cambiar.keys())
                if len(letras_cambiar) < 7 and event not in letras_cambiar.keys():  # si la cantidad de letras a cambiar es menor que 7 y no elegi esa letra para cambiar(evitar cambiar varias veces la misma letra)
                    letras_cambiar[event] = letra  # actualizo el diccionario de las letras a cambiar
                    window[event].Update(button_color=('red', 'lightblue'))  # cambio el color para que el usuario note que letras ya eligio
                    sg.popup("Las letras a cambiar son: "+str(list(letras_cambiar.values())))  # informo que letras by a cambiar
                    window[("cambio"), ].Update("Cambiar "+str(len(letras_cambiar))+" letras.")  # actualizo el boton de cambiar
                elif not len(letras_cambiar) < 7:  # si quiero cambiar mas de la cantidad de mis letras
                    sg.popup("No puede cambiar mas de la cantidad de sus letras.")
                elif event in letras_cambiar.keys():  #  si la posicion de la letra ya se encuentra
                    sg.popup("No puede cambiar la misma letra 2 veces")
            elif event[0] == "cambio":  # si quiero cambiar
                if len(letras_cambiar) > 0:  # si tengo alguna letra que cambiar
                    letras_viejas = list(letras_cambiar.values())  # uso una variable auxiliar para las letras viejas
                    pos_letras = list(letras_cambiar.keys())  # uso una variable auxiliar para las posiciones
                    letras_nuevas = bolsa.sacar_letras(len(letras_viejas))  # saco de la bolsa la cantidad de letras que quiero cambiar
                    if len(letras_nuevas) == len(letras_cambiar):  # si la cantidad de letras nuevas es igual a la cantidad de letras viejas
                        for i in range(len(pos_letras)):  # recorro las posiciones
                            window[pos_letras[i]].Update(letras_nuevas[i])  # actualizo las posiciones con las letras nuevas
                            window[pos_letras[i]].Update(button_color=('black', 'lightblue'))
                        self._letras.update(dict(zip(pos_letras, letras_nuevas)))  # actualizo las letras del jugador
                        window[("vaciar"), ].set_size((5, 3))
                        window[("vaciar"), ].Update("Deshacer")
                        window[("cambio"), ].set_size((5, 3))
                        window[("cambio"), ].Update("Cambiar letras")
                        fin = True  # termino
                else:
                    sg.popup("No eligio letras a cambiar")
            elif event[0] == "vaciar":
                window[("vaciar"), ].set_size((5, 3))
                window[("vaciar"), ].Update("Deshacer")
                window[("cambio"), ].set_size((5, 3))
                window[("cambio"), ].Update("Cambiar letras")
                fin = True  # termino
            elif not(event[0] in self._letras.keys() and letra in self._letras.values()):
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
            # color = window[event].Get()
            # sg.Popup(color)
            if (event == None):  # si el evento es salir
                break  # rompo el ciclo
            letra = window.FindElement(event).GetText()  # obtengo el texto del evento
            event_letra = event  # guardo el evento de la letra que tome
            print("la letra es "+str(letra))
            print(event_letra in self._letras.keys() and letra in self._letras.values())
            if event_letra in self._letras.keys() and letra in self._letras.values():  # si esta en mis letras
                event, values = window.Read()  # leo un lugar donde voy a poner la letra
                if(window.FindElement(event).GetText() == " ") and (event not in self._letras.keys() and self.sigue(posiciones, event[0])):  # si esta vacio y no es el espacio de una letra y sigue(col o fila)
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
            # print("la Palabra es "+str(palabra))
            # print("las posiciones son "+str(posiciones))
            elif event[0] == "vaciar":  # si me equivoque y quiero que me devuelva todas las letras
                palabra, posiciones = self.resetear(posiciones, window)
            elif event[0] == "cambio":  # si quiero cambiar las letras
                self.cambiar_letras(window, bolsa)
            elif event[0] == "fin-turno":  # si quiero terminar el turno
                if len(palabra) >= 2:  # si la palabra tiene 2 o mas letras
                    if self._verificar_juez(palabra, juez):  # la verifico con el juez
                        juez.turno = "maquina"  # le doy el turno a la maquina
                        fin = True  # termine mi turno
                    else:  # si no es una palabra valida
                        palabra, posiciones = self.resetear(posiciones, window)  # devuelvo las letras usadas
                else:
                    sg.popup("La palabra debe contener al menos 2 letras")
