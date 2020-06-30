tablero_facil = []
for i in range(Filas):
    a = []
    for j in range(Columnas):
        if ((i%2 == Filas%2) and (j%2 == Columnas%2)):
            a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'green')))
        else:
            if ((i%2 == 0)&(j%2 == 1))or((i%2 == 1)&(j%2 == 0)):
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'blue')))
            else:
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1)))
    tablero_facil.append(a)
tablero_medio = []
for i in range(Filas):
    a = []
    for j in range(Columnas):
        if (i==0 and j==0)or(i==Filas-1 and j==Columnas-1)or(i==0 and j==Columnas-1)or(i==Filas-1 and j==0):
            a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'green')))
        else:
            if ((i%2 == 0)&(j%2 == 1)):
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'blue')))
            elif ((i%2 == 1)&(j%2 == 0)):
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'red')))
            else:
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1)))
    tablero_medio.append(a)
tablero_dificil = []
for i in range(Filas):
    a = []
    for j in range(Columnas):
        if (i==0 and j==0)or(i==Filas-1 and j==Columnas-1)or(i==0 and j==Columnas-1)or(i==Filas-1 and j==0):
            a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'purple')))
        else:
            if ((i%2 == 0)&(j%2 == 1)):
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'blue')))
            elif ((i%2 == 1)&(j%2 == 0)):
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1), button_color=('white', 'red')))
            else:
                a.append(sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1)))
    tablero_dificil.append(a)
