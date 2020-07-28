"""Este modulo contiene a la clase bolsa que se encargara de dar las letras."""
import random


class Bolsa():
    """Clase Bolsa que genera letras y verifica si esta vacia.

    La longitud del abecedario y de las cantidades coinciden.
    """

    _ABC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    _cant = [11, 3, 4, 4, 11, 2, 2, 2, 6, 2, 1, 4, 3, 5, 1, 8, 2, 1, 4, 7, 4, 2, 6, 1, 1, 1, 1]

    def __init__(self, una_cantidad=[]):
        """Inicializa (constructor) la bolsa."""
        if len(self._ABC) == len(una_cantidad):
            self._cant = una_cantidad

    @property
    def cant(self):
        """Getter de la cantidad."""
        return self._cant

    @cant.setter
    def cant(self):
        """Setter de la cantidad."""
        return self._cant

    @cant.deleter
    def cant(self):
        """Delete de la cantidad."""
        del self._cant

    def esta_vacia(self):
        """Verifica si la bolsa esta vacia osea si no quedan mas letras.

        Recorro el abecedario y si ya no hay ninguna letra devuelvo true
        """
        for i in range(len(self._ABC)):  # recorro de i=0 hasta la longitud del abecedario
            if self._cant[i] > 0:  # si la cantidad en i es distinta de 0
                return False
        return True

    def sacar_letras(self, cantidad):
        """Saca las letras de la bolsa para cada jugador.

        Recibe al objeto y la cantidad de letras que tiene que sacar.
        Devuelve las letras en forma de lista.
        """
        letras = []  # creo una lista vacia para las letras a sacar
        while len(letras) < cantidad:  # mientras que la cantidad de letras no llegue a las que necesito
            posicion = random.randint(0, 26)  # genero un aleatorio para elegir que letra va a salir
            una_letra = self._ABC[posicion]  # genera una letra aleatoria de entre el abecedario
            if self._cant[posicion] > 0:  # si queda de esa letra(ficha) en la bolsa
                letras.append(una_letra)  # agrego la letra a la lista de letras
                self._cant[posicion] -= 1  # disminuyo en uno la cantidad de esa letra
            elif self.esta_vacia():  # sino si la bolsa esta vacia
                break  # rompo el loop
        return letras  # devuelvo la lista de letras

# abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# cant = [11,3,4,4,11,2,2,2,6,2,1,4,1,3,5,1,8,2,1,4,1,7,4,2,6,1,1,1,1]

# print(bolsa)


"""A ×11,
B ×3
C ×4,
D ×4,
E ×11
F ×2,
G ×2
H ×2,
I ×6,
J ×2
K ×1,
L ×4,
M ×3,
N ×5,
Ñ ×1,
O ×8,
P ×2,
Q ×1,
R ×4,
S ×7,
T ×4
V ×2,
U ×6,
W ×1,
X ×1
Y ×1
Z ×1"""
