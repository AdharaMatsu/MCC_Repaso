import csv

def toInt(set):
    for item in range(len(set)):
        for j in range(len(set[item])):
            set[item][j] = int(set[item][j])
    return set

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
# Manhattan
resultados = list()
for fila in range(len(lista)):
    j = 0
    sumatoria = 0
    for columna in range(len(lista[fila])-1):
        sumatoria += abs(lista[fila][columna]-caso1[j])
        j = j + 1
    resultados.append(sumatoria)

print(resultados[0])
#################




