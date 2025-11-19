import csv

def toInt(dataset):
    for item in range(len(dataset)):
        dataset[item] = int(float(dataset[item]))
    return dataset

lista = []
with open('dataset-temp.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for fila in read:
        lista.append(fila)

header = lista.pop(0)

for value in range(len(lista)):
   lista[value][2:]=toInt(lista[value][2:])
#   lista[value] = toInt(lista[value[2:])

for e in lista:
    print(e)

