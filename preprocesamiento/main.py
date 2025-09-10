import csv

def toInt(set):
    for item in range(len(set)):
        for j in range(len(set[item])):
            set[item][j] = int(set[item][j])
    return set

lista = []
with open('tenis_procesado.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for fila in read:
        lista.append((fila[1:]))

header = lista.pop(0)

for e in range(0, len(lista)):
    print(lista[e])