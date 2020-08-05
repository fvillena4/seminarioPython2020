import pattern.es as pt
import PySimpleGUI as sg
import random
from bolsa_letras import Bolsa
from tableros import Tablero
from jugador import Jugador
from juez import Juez
import crear_layout as crear
import menu
from maquina import Maquina


def iniciar(nombre):
    x = random.randint(0, 1)
    if x == 0:
        sg.popup_ok("Comienza el jugador: " + nombre)
        return True, nombre
    else:
        sg.popup_ok("Comienza a jugar la maquina")
        return True, "maquina"


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
layout = menu.layout
config = menu.config
bolsa = Bolsa(un_ABC=config["cant_letras"])
letras_jugador = bolsa.sacar_letras(7)
letras_maquina = bolsa.sacar_letras(7)
guido = Maquina(unas_letras=letras_maquina, un_nivel=config["dificultad"], filas=config["Filas"], columnas=config["Columnas"])
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
# window.Maximize()
a = []
claves = []
for j in range(7):
    clave = "letra" + str(j)
    window[clave].Update(letras_jugador[j])
    claves.append(clave)

mis_letras = dict(zip(claves, letras_jugador))
comenzo = False
final = False
while not final:
    event, values = window.Read()
    if event == None or event == "fin-partida":
        break
    elif event == "iniciar" and not comenzo:
        nombre = sg.popup_get_text("Ingrese su nombre: ")
        jugador = Jugador(nombre, mis_letras, config["dificultad"], config["Filas"], config["Columnas"])
        comenzo, primero = iniciar(nombre)
        juez = Juez(config["dificultad"], config['valores_letras'],config["tablero"], nombre, primero)
    elif not comenzo:
        sg.popup_ok("Para comenzar oprima el boton iniciar")
    if comenzo:
        #while not final:
        if event == None or event == "fin-partida":
            final = True
            sg.Popup("Termino la partida, porque puso fin el usuario.")
            break
        if(juez.turno == nombre):
            jugador.jugar(window, juez, bolsa)
            agregue = jugador._agregar_letras(window, bolsa)
            if not agregue:
                sg.Popup("No se pudo agregar letras.")
                sg.Popup("Termino la partida, porque no hay mas letras.")
                final = True
        if(juez.turno == "maquina"):
            jugue, motivo = guido._jugar(window, juez, config)
            if not jugue:
                if motivo == "no hay espacios":
                    final = True
                    sg.Popup("Termino la partida por la maquina no encontro espacio.")
                elif motivo == "no hay palabras validas":
                    juez.turno = nombre
            else:
                guido.agregar_letras(bolsa.sacar_letras(7-len(guido.letras)))
                juez.turno = nombre
podio = juez._determinar_ganador()
if 0 in podio.keys():
    sg.Popup("Hubo un empate con: "+str(podio[0][0][1])+" puntos.")
else:
    sg.Popup("El ganador es: "+str(podio[1][0])+" con "+str(podio[1][1])+" puntos.")
