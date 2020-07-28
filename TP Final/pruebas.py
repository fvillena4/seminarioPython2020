import PySimpleGUI as sg
filas = 8
columnas = 8

def sigue_fila(act,sig):
    """Esta funcion recible 2 tuplas como parametro (filas, columnas) y analiza si se
       mantiene en la misma fila y avanza por la columna.
       Devuelve True si sigue y sino devuelve False
    """
    return (act[0] == sig[0] and act[1]+1 == sig[1])#si me mantengo en la misma fila y subo la columna

def sigue_col(act,sig):
    """Esta funcion recible como parametro 2 tuplas (filas, columnas) y analiza si se
       mantiene en la misma columna y avanza por la fila.
       Devuelve True si sigue y sino devuelve False
    """
    if(act[0]+1==sig[0] and act[1]==sig[1]):
        #print("la posicion "+str(sig)+" sigue a la posicion "+str(act))
        return True
    else:
        return False

def buscar_espacio(window):
    """Esta función recibe el tablero de juego (window) y devuelve una lista con todas
       las posiciones disponibles para agregar letras (casilleros vacios).
    """
    posiciones = []  #inicializo una lista de posiciones vacia
    for i in range(filas):  #de 0 hasta las filas
        for j in range(columnas):  #de 0 hasta las columnas
            pos = (i, j)  #armo una tupla con i(filas),j(columnas) que representa la posicion
            if (window.FindElement(pos).GetText() == " "): #si el texto del elemento 'pos' es ' '(vacio)
                posiciones.append(pos)  #agrego la posicion a la lista de posiciones
    return posiciones  #devuelvo la lista de posiciones disponibles

def elegir_posicion_fila(posiciones):
    """Esta función devuelve una diccionario con opciones para poner las palabras horizontalmente (de izq a der);
       las claves seran la longitud de los casilleros vacios donde se pueden insertar las palabras y los valores seran
       una lista de tuplas con cada posicion ordenada de izq a der.
    """
    posiciones.sort(key=lambda tup: tup[0])  #ordeno las posiciones segun las filas
    secuencia_fila = []  #inicializo una lista de secuencia de fila
    espacios_palabra = dict()  #creo un diccionario que contendra los espacios vacios y como clave su longitud
    for i in range(len(posiciones)-1):  #de 0  hasta la longitud de las posiciones - 1
        secuencia_fila.append(posiciones[i])  #agrego la posicion en 'i'
        if (sigue_fila(posiciones[i], posiciones[i+1])):    #si sigue fila(actual, siguiente)
            secuencia_fila.append(posiciones[i+1])  #agrego el siguiente
        else:   #sino
            secuencia_fila = list(set(secuencia_fila))#convierto la secuencia de fila en un conjunto(set) para eliminar posibles repetidos y lo vuelvo a convertir a lista
            secuencia_fila.sort(key=lambda tup: tup[1])#ordeno la secuencia de filas segun las columnas
            if(len(secuencia_fila)>=3):#si la longitud de la lista de tuplas es mayor o igual a 3
                dicc = dict()#creo un diccionario auxiliar
                dicc[len(secuencia_fila)] = secuencia_fila#ingreso como clave la longitud de la palabra y como valor la lista de tuplas
                espacios_palabra.update(dicc)#actualizo el diccionario de espacios (si ya existe una clave asi la actualizo por el mas reciente)
            secuencia_fila = []#vacio la lista
        if(i==len(posiciones)-2):#si estoy en el anteultimo caso
            secuencia_fila = list(set(secuencia_fila))
            secuencia_fila.sort(key=lambda tup: tup[1])
            if(len(secuencia_fila)>=3):
                dicc = dict()
                dicc[len(secuencia_fila)] = secuencia_fila
                espacios_palabra.update(dicc)
            secuencia_fila = []
    return espacios_palabra#devuelvo el diccionario

def elegir_posicion_col(posiciones):
    """Esta función devuelve una diccionario con opciones para poner las palabras verticalmente (de arriba a abajo);
       las claves seran la longitud de los casilleros vacios donde se pueden insertar las palabras y los valores seran
       una lista de tuplas con cada posicion ordenada de izq a der.
    """
    posiciones.sort(key=lambda tup: tup[1])#ordeno las posiciones segun las columnas
    secuencia_col = []#inicializo una lista de secuencia de fila
    espacios_palabra = dict()#creo un diccionario que contendra los espacios vacios y como clave su longitud
    for i in range(len(posiciones)-1):#de 0  hasta la longitud de las posiciones - 1
        secuencia_col.append(posiciones[i])#agrego la posicion en 'i'
        if (sigue_col(posiciones[i],posiciones[i+1])):#si sigue fila(actual, siguiente)
            secuencia_col.append(posiciones[i+1])#agrego el siguiente
        else:
            secuencia_col = list(set(secuencia_col))#convierto la secuencia de fila en un conjunto(set) para eliminar posibles repetidos y lo vuelvo a convertir a lista
            secuencia_col.sort(key=lambda tup: tup[0])#ordeno la secuencia de filas segun las filas
            if(len(secuencia_col)>=3):#si la longitud de la lista de tuplas es mayor o igual a 3
                dicc = dict()#creo un diccionario auxiliar
                dicc[len(secuencia_col)] = secuencia_col#ingreso como clave la longitud de la palabra y como valor la lista de tuplas
                espacios_palabra.update(dicc)#actualizo el diccionario de espacios (si ya existe una clave asi la actualizo por el mas reciente)
            secuencia_col = []#vacio la lista
        if(i==len(posiciones)-2):#si estoy en el anteultimo caso
            secuencia_col = list(set(secuencia_col))
            secuencia_col.sort(key=lambda tup: tup[0])
            dicc = dict()
            dicc[len(secuencia_col)] = secuencia_col
            if(len(secuencia_col)>=3):
                espacios_palabra.update(dicc)
            secuencia_col = []
    return espacios_palabra


layout = [[sg.Button(" ", size=(2, 2), key=(i,j), pad=(1,1)) for j in range(filas)] for i in range(columnas)]
window = sg.Window('Tablero', layout, resizable=True, element_justification='c')

while True:
    event, values = window.Read()
    for i in range(4):
        for j in range(6):
            event = i,j
            window.FindElement(event).Update(event)
    """event = (0,2)
    window.FindElement(event).Update("h")
    event = (2,1)
    window.FindElement(event).Update("h")
    event = (1,0)
    window.FindElement(event).Update("h")
    event = (1,1)
    window.FindElement(event).Update("h")
    event = (3,1)
    window.FindElement(event).Update("h")
    event = (4,1)
    window.FindElement(event).Update("h")
    event = (5,1)
    window.FindElement(event).Update("h")
    event = (6,1)
    window.FindElement(event).Update("h")
    event = (0,6)
    window.FindElement(event).Update("h")"""
    event, values = window.Read()
    break
lista = buscar_espacio(window)
print(lista)
print("Las posibles posiciones horizontales son "+str(elegir_posicion_fila(lista)))
print("Las posibles posiciones verticales son "+str(elegir_posicion_col(lista)))
