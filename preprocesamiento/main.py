import csv
lista = []
with open('tenis.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for fila in read:
        #print(fila)
        lista.append(fila)

print(lista)
print(lista[0])
print(lista[1][1])