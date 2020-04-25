#Revisar todo el ejercicio
imagenes = ['im1','im2','im3']
lista = []

for i in range(3):
    x = int(input('ingrese la coordenada x'+str(i+1)+': '))
    y = int(input('ingrese la coordenada y'+str(i+1)+': '))
    tup = (x,y)
    lista.append(tup)
#Falta verificar que no sean repetidas
dicc = {lista[0]:imagenes[0],lista[1]:imagenes[1],lista[2]:imagenes[2]}

print (dicc)
