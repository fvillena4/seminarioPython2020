"""Este programa crea la clase Juez que mediara el juego."""

import pattern.es as ptn

import PySimpleGUI as sg


class Juez():
    """Esta clase actuara como arbitro del juego."""

    _nivel = str()
    _tabla_puntajes = dict()
    _jugadores = dict()
    _turno = str()

    # clasificaciones posibles para adjetivos y verbos
    _TIPO = {'adj': ["AO", "JJ", "AQ", "DI", "DT"],
             'verb': ["VAG", "VBG", "VAI", "VAN", "MD", "VAS", "VMG", "VMI", "VB",
                      "VMM", "VMN", "VMP", "VBN", "VMS", "VSG",
                      "VSI", "VSN", "VSP", "VSS"]
             }

    def __init__(self, un_nivel="facil", una_tabla_puntaje={}, multiplicadores={}, un_jugador="Jugador 1", un_turno="maquina"):
        """Inicializa(Constructor) la clase Juez."""
        self._nivel = un_nivel
        self._tabla_puntaje = una_tabla_puntaje
        self._multiplicadores = multiplicadores
        self._jugadores[un_jugador] = 0
        self._jugadores["maquina"] = 0
        self._turno = un_turno

    @property
    def turno(self):
        """Getter del turno."""
        return self._turno

    @turno.setter
    def turno(self, un_turno):
        """Setter del turno."""
        self._turno = un_turno

    @turno.deleter
    def turno(self):
        """Deleter del turno."""
        del self._turno

    def _es_palabra(self, palabra):
        """Verifica si es una palabra válida segun los diccionarios de pattern.

        Recibe palabra que es un string
        devuelve True si es, False caso contrario.
        """
        return palabra in ptn.lexicon and palabra in ptn.spelling  # devuelve si esta en lexicon y en spelling

    def _clasifico(self, palabra):
        """Función que recibe una palabra y verifica que sea adjetivo o verbo.

        Parametros=
            :palabra: es un string
            :clasificacion: un diccionario que tiene las clasficaciones que busco
        Devuelve True si está dentro de la clasificación, False caso contrario.
        """
        palabra_parseada = (ptn.parse(palabra)).split()  # parseo la palabra y la divido
        for cada in palabra_parseada:  # recorro la palabra parseada
            for i in cada:
                for tipo in self._TIPO:
                    if i[1] in self._TIPO[tipo]:
                        return True
        return False

    def _validar(self, palabra):
        """Valida una palabra segun el nivel del juego."""
        palabra = "".join(list(map(str.lower, palabra)))
        if(self._nivel == "facil"):  # si el nivel es facil
            return self._es_palabra(palabra)  # devuelvo si es palabra
        else:  # si el nivel es medio o dificil
            if(self._es_palabra(palabra)):  # si es palabra
                return self._clasifico(palabra)  # devuelvo si es adjetivo o verbo

    def _calcular_puntaje(self, letras_palabra, posiciones, id):
        """Calcula el puntaje de una palabra.
        Recibe: letras_palabra que es una lista de las letras de la palabra
                ingresada, y la ventana para verificar los descuentos
                y duplicados.
        Actualiza el puntaje del jugador y la maquina.
        Devuelve: el puntaje de la palabra.
        """
        letras_palabra = list(map(str.upper, letras_palabra))
        puntaje = 0  # inicializo el puntaje de la palabra
        if len(letras_palabra) == len(posiciones):
            for i in range(len(letras_palabra)):  # recorro la lista de letras de palabra
                puntaje = self._tabla_puntaje[letras_palabra[i]] * self._multiplicadores[posiciones[i]]  # actualizo el puntaje
        self._jugadores[id] = self._jugadores[id] + puntaje  # actualizo el puntaje del jugador
        sg.Popup(self._jugadores[id])
        return puntaje  # devuelve el puntaje

    def _determinar_ganador(self):
        """Determina el ganador del juego.
        Compara los puntajes del jugador y de la maquina"""
        puestos = dict()  # creo un diccionario vacio para los puestos
        nombres = list(self._jugadores.keys())  # obtengo los nombres de los jugadores (0= el jugador y 1= la maquina)
        if self._jugadores[nombres[0]] > self._jugadores[nombres[1]]:  # si el jugador(0) tiene mas punto que la maquina(1)
            puestos[1] = [nombres[0], self._jugadores[nombres[0]]]  # puesto1 = jugador , su puntaje (gana el jugador)
            puestos[2] = [nombres[1], self._jugadores[nombres[1]]]  # puesto2 = maquina , su puntaje
        elif self._jugadores[nombres[0]] < self._jugadores[nombres[1]]:  # si el jugador tiene menos puntos que la maquina
            puestos[1] = [nombres[1], self._jugadores[nombres[1]]]  # puesto1 = maquina , su puntaje (gana la maquina)
            puestos[2] = [nombres[0], self._jugadores[nombres[0]]]  # puesto2 = jugador , su puntaje
        else:  # si estan empatados
            puestos[0] = [[nombres[0], self._jugadores[nombres[0]]], [nombres[1], self._jugadores[nombres[1]]]]  # en la posicion 0 devuelvo a ambos
        return puestos
