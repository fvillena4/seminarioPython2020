"""Este modulo construye a la maquina para jugar."""

from itertools import permutations

import time

import pattern.es as ptn

import PySimpleGUI as sg

from bolsa_letras import Bolsa

from juez import Juez

FILAS = 8
COLUMNAS = 8


class Maquina():
    """Clase Maquina que forma palabras y las pone en el tablero."""

    _nivel = str()
    _letras = list()
    _palabras_validas = list()
    _palabras_adj_verb = list()
    _espacios = dict()

    def __init__(self, unas_letras, un_nivel='facil'):
        """Inicializa (Constructor) la maquina."""
        self._nivel = un_nivel  # recibo un nivel (facil,medio,dificil) para saber como tiene que jugar la maquina
        self._letras = unas_letras

    @property
    def nivel(self):
        """Getter del nivel."""
        return self._nivel

    @nivel.setter
    def nivel(self, un_nivel):
        """Setter del nivel."""
        self._nivel = un_nivel

    @nivel.deleter
    def nivel(self):
        """Delete del nivel."""
        del self._nivel

    @property
    def letras(self):
        """Getter del nivel."""
        return self._letras

    @letras.setter
    def letras(self, unas_letras):
        """Setter del nivel."""
        self._letras = unas_letras

    @letras.deleter
    def letras(self):
        """Delete del nivel."""
        del self._letras

    def agregar_letras(self, nuevas_letras):
        self._letras.extend(nuevas_letras)

    def armo_palabra(self):
        """Arma palabras combinando todas las letras.

        Armo las posibles combinaciones y permutaciones con una lista de
        letras recibidas.
        Recibe letras: lista de letras
        Devuelve una lista con las palabras armadas
        """
        palabras = set()  # palabras es un conjunto sin repetir
        for i in range(2, len(self._letras) + 1):  # de i=2 hasta la cantidad de letras+1
            palabras.update((map("".join, permutations(self._letras, i))))  # generamos las palabra con posibles combinaciones de las letras
        return list(palabras)  # devuelvo el conjunto de palabras

    def _validar_palabras(self, palabras, juez):
        """Valida las palabras que formo con las letras de la maquina.

        Se comunica con el Juez y le pregunta si es una pregunta valida
        y si lo es la agrega.
        Devuelve la lista de palabras vallidas segun el nivel
        """
        if(self._nivel == "facil"):  # si el nivel es facil
            palabras_facil = []
            for i in palabras:
                if juez._validar(i):  # si el juez considera que es una palabra
                    palabras_facil.append(i)  # la agrego
            return palabras_facil
        else:  # si el nivel es medio o dificil
            palabras_medio_dificil = []
            for i in palabras:
                if juez._validar(i):  # devuelvo si es palabra
                    palabras_medio_dificil.append(i)
            return palabras_medio_dificil

    def sigue_fila(self, act, sig):
        """Verifica si mantiene la fila y mueve la columna.

        Recibe 2 tuplas como parametro (filas, columnas) y
        analiza si se mantiene en la misma fila y avanza por la columna.
        Devuelve True si sigue y sino devuelve False
        """
        return (act[0] == sig[0] and act[1]+1 == sig[1])  # si me mantengo en la misma fila y subo la columna

    def sigue_col(self, act, sig):
        """Verifica si mantiene la columna y mueve la fila.

        Recibe como parametro 2 tuplas (filas, columnas) y
        analiza si semantiene en la misma columna y avanza por la fila.
        Devuelve True si sigue y sino devuelve False
        """
        return (act[0]+1 == sig[0] and act[1] == sig[1])

    def buscar_espacio(self, window):
        """Busca todos los espacios vacios de un tablero.

        Recibe el tablero de juego (window) y devuelve una
        lista con todas las posiciones disponibles para agregar
        letras (casilleros vacios).
        """
        posiciones = []  # inicializo una lista de posiciones vacia
        for i in range(FILAS):  # de 0 hasta las filas
            for j in range(COLUMNAS):  # de 0 hasta las columnas
                pos = (i, j)  # armo una tupla con i(filas),j(columnas) que representa la posicion
                if (window.FindElement(pos).GetText() == " "):  # si el texto del elemento 'pos' es ' '(vacio)
                    posiciones.append(pos)  # agrego la posicion a la lista de posiciones
        return posiciones  # devuelvo la lista de posiciones disponibles

    def elegir_posicion_fila(self, posiciones):
        """Elige una posicion horizontal libre en el tablero.

        Devuelve una diccionario con opciones para poner
        las palabras horizontalmente (de izq a der);
        Las claves seran la longitud de los casilleros vacios donde se
        pueden insertar las palabras y los valores seran
        una lista de tuplas con cada posicion ordenada de izq a der.
        """
        posiciones.sort(key=lambda tup: tup[0])  # ordeno las posiciones segun las filas
        secuencia_fila = []  # inicializo una lista de secuencia de fila
        espacios_palabra = dict()  # creo un diccionario que contendra los espacios vacios y como clave su longitud
        for i in range(len(posiciones)-1):  # de 0  hasta la longitud de las posiciones - 1
            secuencia_fila.append(posiciones[i])  # agrego la posicion en 'i'
            if (self.sigue_fila(posiciones[i], posiciones[i+1])):  # si sigue fila(actual, siguiente)
                secuencia_fila.append(posiciones[i+1])  # agrego el siguiente
            else:
                secuencia_fila = list(set(secuencia_fila))  # convierto la secuencia de fila en un conjunto(set) para eliminar posibles repetidos y lo vuelvo a convertir a lista
                secuencia_fila.sort(key=lambda tup: tup[1])  # ordeno la secuencia de filas segun las columnas
                if(len(secuencia_fila) >= 2):  # si la longitud de la lista de tuplas es mayor o igual a 3
                    dicc = dict()  # creo un diccionario auxiliar
                    dicc[len(secuencia_fila)] = secuencia_fila  # ingreso como clave la longitud de la palabra y como valor la lista de tuplas
                    espacios_palabra.update(dicc)  # actualizo el diccionario de espacios (si ya existe una clave asi la actualizo por el mas reciente)
                secuencia_fila = []  # vacio la lista
            if i == len(posiciones)-2:  # si estoy en el anteultimo caso
                secuencia_fila = list(set(secuencia_fila))
                secuencia_fila.sort(key=lambda tup: tup[1])
                if len(secuencia_fila) >= 2:
                    dicc = dict()
                    dicc[len(secuencia_fila)] = secuencia_fila
                    espacios_palabra.update(dicc)
                secuencia_fila = []
        self._espacios = espacios_palabra
        return espacios_palabra  # devuelvo el diccionario

    def elegir_posicion_col(self, posiciones):
        """Elige una posicion vertical libre en el tablero.

        Devuelve una diccionario con opciones para poner
        las palabras verticalmente (de arriba a abajo);
        Las claves seran la longitud de los casilleros vacios donde se
        pueden insertar las palabras y los valores seran
        una lista de tuplas con cada posicion ordenada de izq a der.
        """
        posiciones.sort(key=lambda tup: tup[1])  # ordeno las posiciones segun las columnas
        secuencia_col = []  # inicializo una lista de secuencia de fila
        espacios_palabra = dict()  # creo un diccionario que contendra los espacios vacios y como clave su longitud
        for i in range(len(posiciones)-1):  # de 0  hasta la longitud de las posiciones - 1
            secuencia_col.append(posiciones[i])  # agrego la posicion en 'i'
            if (self.sigue_col(posiciones[i], posiciones[i+1])):  # si sigue fila(actual, siguiente)
                secuencia_col.append(posiciones[i+1])  # agrego el siguiente
            else:
                secuencia_col = list(set(secuencia_col))  # convierto la secuencia de fila en un conjunto(set) para eliminar posibles repetidos y lo vuelvo a convertir a lista
                secuencia_col.sort(key=lambda tup: tup[0])  # ordeno la secuencia de filas segun las filas
                if(len(secuencia_col) >= 2):  # si la longitud de la lista de tuplas es mayor o igual a 3
                    dicc = dict()  # creo un diccionario auxiliar
                    dicc[len(secuencia_col)] = secuencia_col  # ingreso como clave la longitud de la palabra y como valor la lista de tuplas
                    espacios_palabra.update(dicc)  # actualizo el diccionario de espacios (si ya existe una clave asi la actualizo por el mas reciente)
                secuencia_col = []  # vacio la lista
            if i == len(posiciones)-2:  # si estoy en el anteultimo caso
                secuencia_col = list(set(secuencia_col))
                secuencia_col.sort(key=lambda tup: tup[0])
                dicc = dict()
                dicc[len(secuencia_col)] = secuencia_col
                if len(secuencia_col) >= 2:
                    espacios_palabra.update(dicc)
                secuencia_col = []
        self._espacios = espacios_palabra
        return espacios_palabra

    def _jugar(self, window):
        """Elige la mejor palabra y busca el espacio mas grande.

        En el nivel facil: elijo la 1ª palabra posible que encuentre
        En los otros niveles: elijo la palabra mas grande posible.
        Devuelvo True si pude poner la palabra o False si no.
        """
        palabra = ""
        if (self._espacios.keys()):
            espacio_max = max(list(self._espacios.keys()))
        else:
            espacio_max = 0
        if(self._nivel == "facil"):
            for i in self._palabras_validas:  # recorro las palabras validas
                if espacio_max >= len(i):  # si encuentro un lugar donde pueda entrar
                    palabra = i  # guardo la 1ª palabra que cumpla la condición
                    break  # salgo del ciclo
        else:
            adj_verb = sorted(self._palabras_adj_verb, key=len, reverse=True)  # creo una variable auxiliar con la lista de palabras ordenadas de mayora a menor
            for i in adj_verb:
                if espacio_max >= len(palabra):  # si encuentro un lugar donde pueda entrar
                    palabra = i  # guardo la palabra mas grande posible
                    break  # salgo del ciclo
        if len(self._espacios.keys()) > 0 and espacio_max >= len(palabra):
            self._poner_palabra(list(palabra), self._espacios[espacio_max], window)
            return True  # devuelvo si pude poner la palabra
        else:
            return False


    def _eliminar_letras(self, letras):
        """Elimina las letras disponibles de la maquina """
        for i in letras:  # recorro las letras que use
            self._letras.remove(i)  # elimino las letras


    def _poner_palabra(self, letras, posiciones, window):
        """Pone la palabra(letras) en tablero(window).

        Recorre la lista donde se van a ubicar las letras
        y actualiza el tablero.
        """
        for i in range(len(letras)):  # desde i hasta la cantidad de las posiciones
            # time.sleep(1)
            window[posiciones[i]].update(letras[i])  # modifico la letra en la posicion elegida
        self._eliminar_letras(letras)  # elimino la letra que agregue de la lista de letras
        return True

# clasificaciones posibles para adjetivos y verbos
TIPO = {'adj': ["AO", "JJ", "AQ", "DI", "DT"],
        'verb': ["VAG", "VBG", "VAI", "VAN", "MD", "VAS", "VMG", "VMI", "VB",
                 "VMM", "VMN", "VMP", "VBN", "VMS", "VSG",
                 "VSI", "VSN", "VSP", "VSS"]
        }


def clasifico(palabra, clasificacion):
    """Función que recibe una palabra y verifica que sea adjetivo o verbo.

    Parametros=
        :palabra: es un string
        :clasificacion: un diccionario que tiene las clasficaciones que busco
    Devuelve True si está dentro de la clasificación, False caso contrario.
    """
    palabra_parseada = (ptn.parse(palabra)).split()  # parseo la palabra y la divido
    for cada in palabra_parseada:
        for i in cada:
            for tipo in clasificacion:
                if i[1] in clasificacion[tipo]:
                    return True
    return False


def es_palabra(palabra):
    """Verifica si es una palabra válida segun los diccionarios de pattern.

    Recibe palabra que es un string
    devuelve True si es, False caso contrario.
    """
    return palabra in ptn.lexicon and palabra in ptn.spelling


# lista_letras = ['a', 'e', 'b', 'a', 's', 'c', 'm']

bolsa = Bolsa()
lista_letras = bolsa.sacar_letras(7)
guido = Maquina(unas_letras=lista_letras, un_nivel="dificil")
arbitro = Juez("dificil")
layout = [[sg.Button(" ", size=(2, 2), key=(i, j), pad=(1, 1)) for j in range(FILAS)] for i in range(COLUMNAS)]
window = sg.Window('Tablero', layout, resizable=True, element_justification='c')

while True:
    lista_palabras = guido.armo_palabra()
    guido._palabras_adj_verb = guido._validar_palabras(lista_palabras, arbitro)
    # guido._palabras_adj_verb = []
    # guido._palabras_validas = []
    # for pal in lista_palabras:
    #     if es_palabra(pal):
    #         guido._palabras_validas.append(pal)
    #         if clasifico(pal, TIPO):
    #             guido._palabras_adj_verb.append(pal)
    event, values = window.Read()
    for i in range(4):
        for j in range(4):
            event = i, j
            window.FindElement(event).Update(event)
    lista = guido.buscar_espacio(window)
    espacios = guido.elegir_posicion_fila(lista)
    juge = guido._jugar(window)
    if not juge:
        espacios = guido.elegir_posicion_col(lista)
        juge = guido._jugar(window)
    guido.agregar_letras(bolsa.sacar_letras(7-len(guido.letras)))
    # break
