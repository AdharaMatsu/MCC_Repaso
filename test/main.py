import random as rnd

#rnd.seed(10)
n = int(input())
matriz = []
vueltas = int(input())

for e in range(n):
    lista = []
    for i in range(n):
        lista.append(rnd.randint(35, 99))
    matriz.append(lista)

x = 0
y = 0
while vueltas > 0:
    opcion = rnd.randint(0, 100)
    if opcion < 50: # Fracaso
        matriz[x][y] = opcion - 2.8
    else: # Exito
        matriz[x][y] = opcion + 2.2

        
    vueltas -= 1

