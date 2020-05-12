import hangman
import reversegam
import tictactoeModificado
from collections import defaultdict
import json
import PySimpleGUI as sg

sg.ChangeLookAndFeel('DarkAmber')
juegos = ("Ahorcado", "TA-TE-TI", "Otello")
layout = [[sg.Text('Biblioteca')],
          [sg.Text('Elegí cual juego querés jugar:')],
          [sg.Listbox(juegos, size=(20, len(juegos)), key='-JUEGO-')],
          [sg.Button('Jugar'), sg.Button('Salir')]]



def identificador(dicc, name, juego):
    dicc[name].append(juego)
    return dicc


def main(args):
    name = input('Ingrese su nombre: ')
    dicc = defaultdict(list)
    window = sg.Window('Steam', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Salir'):   # if user closes window or clicks cancel
            break
        elif event in "Jugar":
            eleccion = values['-JUEGO-'][0]
            if eleccion == "Ahorcado":
                juego = "Ahorcado"
                dicc = identificador(dicc, name, juego)
                hangman.main()
            elif eleccion == "TA-TE-TI":
                juego = "Ta-Te-Ti"
                dicc = identificador(dicc, name, juego)
                tictactoeModificado.main()
            elif eleccion == "Otello":
                juego = "Otello"
                dicc = identificador(dicc, name, juego)
                reversegam.main()
        with open("jugadores.json", 'a') as file:
            json.dump(dicc, file, indent=2)
    window.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

    """while sigo_jugando:
        print('''
        Elegí con qué juego querés jugar:
        1.- Ahorcado
        2.- Ta-TE-TI
        3.- Otello
        4.- Salir''')
        opcion = input()
        if opcion == '1':
            juego = "Ahorcado"
            dicc = identificador(dicc, name, juego)
            hangman.main()
        elif opcion == '2':
            juego = "Ta-Te-Ti"
            dicc = identificador(dicc, name, juego)
            tictactoeModificado.main()
        elif opcion == '3':
            juego = "Otello"
            dicc = identificador(dicc, name, juego)
            reversegam.main()
        elif opcion == '4':
            sigo_jugando = False
            with open("jugadores.json", 'a') as file:
                json.dump(dicc, file, indent=2)"""
