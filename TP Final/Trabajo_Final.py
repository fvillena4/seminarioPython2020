import pattern
import PySimpleGUI as sg
import random

Filas = 10
Columnas = 10
layout = [[sg.Button("", size=(2, 2), key=(i,j), pad=(1,1)) for j in range(Filas)] for i in range(Columnas)]
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letras=[]
a=[]
for j in range(7):
    print(j)
    letras.append(abc[random.randint(0, 25)])
    a.append(sg.Button(letras[j], size=(3, 3), key=("letra"+str(j)), pad=((1,15),15,1)))

layout.append(a)

window = sg.Window('Tablero').Layout(layout)

while True:
    event, values = window.Read()
    print(event)
    print(values)
    if (event == None):
        break

    letra = window.FindElement(event).GetText()
    event, values = window.Read()
    window.FindElement(event).Update(letra)
