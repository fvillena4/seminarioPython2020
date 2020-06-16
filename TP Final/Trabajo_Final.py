import pattern
import PySimpleGUI as sg
import random

Filas = 10
Columnas = 10
layout = [[sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1)) for j in range(Filas)] for i in range(Columnas)]
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letras=[]
a=[]
for j in range(7):
    letras.append(abc[random.randint(0, 25)])
    a.append(sg.Button(letras[j], size=(3, 3), key=("letra"+str(j)), pad=((1,15),15,1)))

layout.append(a)
layout.append([sg.Button('Iniciar', border_width = 5, button_color=('white', 'green'), size=(3, 3), font=("Helvetica", 12)), sg.Button('Finalizar turno', border_width = 5, button_color=('white', 'red'), size=(3, 3), font=("Helvetica", 12))])
window = sg.Window('Tablero').Layout(layout)

while True:
    event, values = window.Read()
    if (event == None):
        break
    letra = window.FindElement(event).GetText()
    event_letra = event
    if (letra in letras):#verifico que este en mis letras, el problema es que si hay una letra igual ya puesta en el tablero la podria modificar y no deberia
        event, values = window.Read()
        if(window.FindElement(event).GetText()==" "):
            window.FindElement(event).Update(letra)
            window.FindElement(event_letra).Update(" ")
        else:
            print("Elija la letra para ingresar")
