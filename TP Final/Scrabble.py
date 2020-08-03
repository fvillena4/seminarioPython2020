import pattern.es as pt
import PySimpleGUI as sg
import random
from bolsa_letras import Bolsa
from tableros import Tablero
from jugador import Jugador
from juez import Juez
import crear_layout as crear
import menu


def iniciar(nombre):
    x = random.randint(0, 1)
    if x == 0:
        sg.popup_ok("Comienza el jugador: " + nombre)
    else:
        sg.popup_ok("Comienza a jugar la maquina")
    return True


def verificarPalabra(palabra):
    """Verifico que la palabra esta en los diccionarios de pattern.
    """
    return palabra in (pt.lexicon and pt.spelling)


def esBotonLetra(cadena):
    """ Funcion que verificaria si el boton es una letra, ya que el event de letras es
        letra+numero
    """
    cadena = cadena[0:5]  # corto el string sin contar el numero
    if cadena == "letra":  # si el string es "letra"
        return True
    else:
        return False


def posicionesPalabra(pos_actual, posiciones, window, event):
    """Verificaria que las letras se vayan ingresando con cierto orden tanto
       como vertical o horizontal. Devuelve una lista de tuplas de las posiciones
       de cada letra en orden. Si el usuario se equivoca debera apretar deshacer y borrar todo
       para que le devuelvan las letras. HAY QUE HACERLO FUNCIONAR PORQUE TIENE ERRORES """
    if (
        len(posiciones) < 1
    ):  # Si tengo menos de una posicion es que no inserte ninguna letra
        posiciones.append(pos_actual)  # agrego la posicion
    elif len(posiciones) >= 1:  # sino si tengo una o mas de una posicion
        pos_ult = len(posiciones) - 1  # asigno cual el la posicion del ultimo
        if (pos_actual[0] == posiciones[pos_ult[0]]) or (pos_actual[1] == posiciones[pos_ult[1]]):  # si esta en la misma fila o columna
            posiciones.append(pos_actual)  # agrego la posicion
        else:
            print("No puede ingresar una letra diagonalmente")
    return posiciones  # devuelvo las posiciones


# tab = Tablero()
# layout = tab.config_tablero()
bolsa = Bolsa()
letras = bolsa.sacar_letras(7)
layout = menu.layout
config = menu.config
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
a = []
claves = []
for j in range(7):
    clave = ("letra" + str(j),)
    window[clave].Update(letras[j])
    claves.append(clave)

mis_letras = dict(zip(claves, letras))
b = []
for j in range(7):
    b.append(sg.Button("*", size=(3, 3), key=("letraM",), button_color=("white", "blue")))

layout.append(a)
layout.insert(0, b)
layout.append(
    [
        sg.Button(
            "Iniciar",
            key=("iniciar",),
            border_width=5,
            button_color=("white", "green"),
            size=(3, 3),
            font=("Helvetica", 12),
        ),
        sg.Button(
            "Finalizar turno",
            key=("fin-turno",),
            border_width=5,
            button_color=("white", "red"),
            size=(5, 3),
            font=("Helvetica", 12),
        ),
        sg.Button(
            "Deshacer",
            key=("vaciar",),
            border_width=5,
            button_color=("black", "pink"),
            size=(5, 3),
            pad=((1, 15), 15, 1),
            font=("Helvetica", 12),
        ),
        sg.Button(
            "Cambiar letras",
            key=("cambio",),
            border_width=5,
            button_color=('black', 'lightblue'),
            size=(5, 3),
            pad=((1, 15), 15, 1),
            font=("Helvetica", 12),
        ),
    ]
)
posiciones = []  # lista que va a tener las posiciones
palabra = []  # lista que va a contener la palabra
juez = Juez("facil")
comenzo = False
while True:
    event, values = window.Read()
    if event in None or event[0] == "fin-partida":
        break
    elif event[0] == "iniciar" and not comenzo:
        nombre = sg.popup_get_text("Ingrese su nombre: ")
        jugador = Jugador(nombre, mis_letras)
        comenzo = iniciar(nombre)
    elif not comenzo:
        sg.popup_ok("Para comenzar oprima el boton iniciar")
    if comenzo:
        jugador.jugar(window, juez, bolsa)
