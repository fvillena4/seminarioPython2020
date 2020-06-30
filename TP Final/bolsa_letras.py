import random

def estaVacia(bolsa):
    """Verifica si la bolsa esta vacia osea si no quedan mas letras
    """
    for i in list(bolsa.keys()):
        if(bolsa[i]!= 0):
            return False
    return True

def generarLetras(bolsa):
    """Esta función a generar las letras disminuyendo hasta llegar a 0 en cada letra
       y verificia que la bolsa no este vacia
    """
    letras=[]
    abc = list(bolsa.keys())
    while len(letras)<7:
        a = abc[random.randint(0, 28)]
        if (bolsa[a]>0):
            letras.append(a)
            bolsa[a] = bolsa[a] - 1
        elif(estaVacia(bolsa)):
            break
    return letras, bolsa

#abc = ["a","b","c","d","e","f","g","h","i","j","k","l","ll","m","n","ñ","o","p","q","r","rr","s","t","u","v","w","x","y","z"]
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cant = [11,3,4,4,11,2,2,2,6,2,1,4,1,3,5,1,8,2,1,4,1,7,4,2,6,1,1,1,1]
bolsa = dict(zip(abc, cant))
#print(bolsa)
letras,bolsa = generarLetras(bolsa)
cant = 0
print(estaVacia(bolsa))
while (not estaVacia(bolsa)):
    cant = cant +1
    print(cant)
    letras,bolsa = generarLetras(bolsa)
print(estaVacia(bolsa))
print(letras)
print(bolsa)

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
LL ×1,
M ×3,
N ×5,
Ñ ×1,
O ×8,
P ×2,
Q ×1,
R ×4,
RR ×1,
S ×7,
T ×4
V ×2,
U ×6,
W ×1,
X ×1
Y ×1
Z ×1"""
