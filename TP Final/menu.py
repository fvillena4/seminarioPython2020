import PySimpleGUI as sg

layout = [
          [sg.Text('SCRABBLE',size=(50, 1), justification="center", pad=(50,50), font=("Arial", 20))],
          [sg.Button('Iniciar', key="iniciar", border_width = 7, button_color=('white', 'lightblue'), size=(50, 3), pad=(30,30), font=("Arial", 12))],
          [sg.Button('Configuración', key="config", border_width = 7, button_color=('white', 'lightblue'), size=(50, 3), pad=(30,30), font=("Arial", 12))],
          [sg.Button('Salir', key="salir", border_width = 7, button_color=('white', 'lightblue'), size=(50, 3), pad=(30,30), font=("Arial", 12))]
         ]

window = sg.Window('Menú', layout, resizable=True, element_justification='c', background_color="#143430")

while True:
    event, values = window.Read()
    print(event)
    if (event == None or event == "salir"):
        break
    if (event == "iniciar"):
        window.close()
        import Scrabble.py
