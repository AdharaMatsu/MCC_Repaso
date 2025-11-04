import csv

def toInt(dataset):
    for item in range(len(dataset)):
        for j in range(len(dataset[item])):
            dataset[item][j] = int(dataset[item][j])
    return dataset

lista = []
with open('Casa de Hogwarts.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for fila in read:
        lista.append(fila[1:])

casas = {'Gryffindor':1, 'Slytherin':2, 'Hufflepuff':3, 'Ravenclaw':4}

header = lista.pop(0)
for fila in lista:
    valor_actual = fila[-1]  # última columna
    fila[-1] = casas[valor_actual]

lista = toInt(lista)

caso1 = [35,28,90,33,43,11,37,59]
print('Clasificador de casa: \n')
print('En escala del 1 al 100%, escriba su:')

caso = []
for fila in range(len(header)-1):
    print('Nivel de ',header[fila])
    caso.append(int(input()))

for fila in range(len(lista)):
    j = 0
    sumatoria = 0
    for columna in range(len(lista[fila])-1):
        sumatoria += abs(lista[fila][columna]-caso[j])
        j = j + 1
    # Cambia los valores
    lista[fila].append(sumatoria)

#################

k = 15

ordenada = sorted(lista, key=lambda x: x[-1])
# Lambda ayuda a definir funciones pequeñas sin nombre
# x es cada sublista (ej: [3, 5], [1, 9], …).
# x[-1]  agarra el ultimo elemento de las listas de la lista como
# criterio para ordenar

seleccion = ordenada[:k]
clases = [fila[-2] for fila in seleccion]
maximo = max(clases, key=clases.count)
for c in casas:
    if casas[c] == maximo:
        print('mmmm... ya see., te pondre en... ',c)
