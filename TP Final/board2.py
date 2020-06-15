import PySimpleGUI as sg
sg.theme('LightGreen3')
layout = [[sg.T('',justification="center")]]
for i in range(15):
    inputs = [sg.Button(size=(1, 1), key=(i,j), pad=(2,2)) for j in range(15)]
    layout.append(inputs)
a = [sg.Button(size=(2, 2), key=("Letra"+str(j)), pad=((10,10),10,10)) for j in range(7)]
layout.append(a)
layout.append([sg.Button('Iniciar', border_width = 5, button_color=('blue', 'red'), size=(3, 3))])
form = sg.FlexForm('Tablero')
form.Layout(layout)

while True:
    button, values = form.Read()
    print(button)
    if button is None:
        break
