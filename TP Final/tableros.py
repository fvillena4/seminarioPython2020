import PySimpleGUI as sg


class Tablero():
    dificultad = "facil"  # Por defecto la dificultad es facil
    filas = 10
    columnas = 10
    layout = []

    def getLayout(self):
        return self.layout

    def setLayout(self, lay):
        self.layout = lay

    def getDificultad(self):
        return self.dificultad

    def setDificultad(self, difi):
        self.dificultad = difi

    def getFilas(self):
        return self.filas

    def setFilas(self, fila):
        self.filas = fila

    def getColumnas(self):
        return self.columnas

    def setFilas(self, colum):
        self.columnas = colum

    def configTablero(self):
        if self.getDificultad() == "facil":
            for i in range(self.getFilas()):
                a = []
                for j in range(self.getColumnas()):
                    if (i % 2 == self.getFilas() % 2) and (
                        j % 2 == self.getColumnas() % 2
                    ):
                        a.append(
                            sg.Button(
                                " ",
                                size=(3, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "green"),
                            )
                        )
                    else:
                        if ((i % 2 == 0) & (j % 2 == 1)) or (
                            (i % 2 == 1) & (j % 2 == 0)
                        ):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=(i, j),
                                    pad=(1, 1),
                                    button_color=("white", "blue"),
                                )
                            )
                        else:
                            a.append(
                                sg.Button(" ", size=(3, 2), key=(i, j), pad=(1, 1))
                            )
                layout.append(a)
        elif self.getDificultad() == "medio":
            for i in range(self.getFilas()):
                a = []
                for j in range(self.getColumnas()):
                    if (
                        (i == 0 and j == 0)
                        or (i == self.getFilas() - 1 and j == self.getColumnas() - 1)
                        or (i == 0 and j == self.getColumnas() - 1)
                        or (i == self.getFilas() - 1 and j == 0)
                    ):
                        a.append(
                            sg.Button(
                                " ",
                                size=(3, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "green"),
                            )
                        )
                    else:
                        if (i % 2 == 0) & (j % 2 == 1):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=(i, j),
                                    pad=(1, 1),
                                    button_color=("white", "blue"),
                                )
                            )
                        elif (i % 2 == 1) & (j % 2 == 0):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=(i, j),
                                    pad=(1, 1),
                                    button_color=("white", "red"),
                                )
                            )
                        else:
                            a.append(
                                sg.Button(" ", size=(3, 2), key=(i, j), pad=(1, 1))
                            )
                layout.append(a)
        elif self.getDificultad() == "dificil":
            for i in range(self.getFilas()):
                a = []
                for j in range(self.getColumnas()):
                    if (
                        (i == 0 and j == 0)
                        or (i == self.getFilas() - 1 and j == self.getColumnas() - 1)
                        or (i == 0 and j == self.getColumnas() - 1)
                        or (i == self.getFilas() - 1 and j == 0)
                    ):
                        a.append(
                            sg.Button(
                                " ",
                                size=(3, 2),
                                key=(i, j),
                                pad=(1, 1),
                                button_color=("white", "purple"),
                            )
                        )
                    else:
                        if (i % 2 == 0) & (j % 2 == 1):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=(i, j),
                                    pad=(1, 1),
                                    button_color=("white", "blue"),
                                )
                            )
                        elif (i % 2 == 1) & (j % 2 == 0):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=(i, j),
                                    pad=(1, 1),
                                    button_color=("white", "red"),
                                )
                            )
                        else:
                            a.append(
                                sg.Button(" ", size=(3, 2), key=(i, j), pad=(1, 1))
                            )
                layout.append(a)
        return layout
