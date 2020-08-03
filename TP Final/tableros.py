import PySimpleGUI as sg


class Tablero():
    _dificultad = "facil"  # Por defecto la dificultad es facil
    _filas = 7
    _columnas = 7
    _layout = []

    @property
    def layout(self):
        return self._layout

    @layout.setter
    def layout(self, lay):
        self._layout = lay

    @property
    def dificultad(self):
        return self._dificultad

    @dificultad.setter
    def dificultad(self, difi):
        self._dificultad = difi

    @property
    def filas(self):
        return self._filas

    @filas.setter
    def filas(self, fila):
        self._filas = fila

    @property
    def columnas(self):
        return self._columnas

    @columnas.setter
    def columnas(self, colum):
        self._columnas = colum

    def config_tablero(self):
        print(self.dificultad)
        if self.dificultad == "facil":
            for i in range(self.filas):
                a = []
                for j in range(self.columnas):
                    if (i % 2 == self.filas % 2) and (
                        j % 2 == self.columnas % 2
                    ):
                        a.append(
                            sg.Button(
                                " ",
                                size=(3, 2),
                                key=((i, j), 3),
                                pad=(1, 1),
                                button_color=("white", "green"),
                            )
                        )
                    else:
                        if ((i % 2 == 0) & (j % 2 == 1)) or (
                            (i % 2 == 1) & (j % 2 == 0)):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=((i, j), 2),
                                    pad=(1, 1),
                                    button_color=("white", "blue"),
                                )
                            )
                        else:
                            a.append(
                                sg.Button(" ", size=(3, 2), key=((i, j), 1), pad=(1, 1))
                            )
                self.layout.append(a)
        elif self.dificultad == "medio":
            for i in range(self.filas):
                a = []
                for j in range(self.columnas):
                    if (
                        (i == 0 and j == 0)
                        or (i == self.filas - 1 and j == self.columnas - 1)
                        or (i == 0 and j == self.columnas - 1)
                        or (i == self.filas - 1 and j == 0)
                    ):
                        a.append(
                            sg.Button(
                                " ",
                                size=(3, 2),
                                key=((i, j), 3),
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
                                    key=((i, j), 2),
                                    pad=(1, 1),
                                    button_color=("white", "blue"),
                                )
                            )
                        elif (i % 2 == 1) & (j % 2 == 0):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=((i, j), 0.5),
                                    pad=(1, 1),
                                    button_color=("white", "red"),
                                )
                            )
                        else:
                            a.append(
                                sg.Button(" ", size=(3, 2), key=((i, j), 1), pad=(1, 1))
                            )
                self.layout.append(a)
        elif self.dificultad == "dificil":
            for i in range(self.filas):
                a = []
                for j in range(self.columnas):
                    if (
                        (i == 0 and j == 0)
                        or (i == self.filas - 1 and j == self.columnas - 1)
                        or (i == 0 and j == self.columnas - 1)
                        or (i == self.filas - 1 and j == 0)
                    ):
                        a.append(
                            sg.Button(
                                " ",
                                size=(3, 2),
                                key=((i, j), 3),
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
                                    key=((i, j), 2),
                                    pad=(1, 1),
                                    button_color=("white", "blue"),
                                )
                            )
                        elif (i % 2 == 1) & (j % 2 == 0):
                            a.append(
                                sg.Button(
                                    " ",
                                    size=(3, 2),
                                    key=((i, j), 0.5),
                                    pad=(1, 1),
                                    button_color=("white", "red"),
                                )
                            )
                        else:
                            a.append(
                                sg.Button(" ", size=(3, 2), key=((i, j), 1), pad=(1, 1))
                            )
                self.layout.append(a)
        return self.layout
