import crear_layout as ly
import PySimpleGUI as sg

layout = ly.crear_lyt("menu")
window = sg.Window(
    "Configuración",
    layout,
    resizable=True,
    element_justification="c",
    background_color="#143430",
)

while True:
    event, values = window.Read()
    print(event)
    if event is None:
        break
window.Close()
