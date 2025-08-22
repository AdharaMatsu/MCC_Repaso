import csv
lista = []
with open('tenis.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for fila in read:
        #print(fila)
        lista.append(fila[1:])

for i in range(1, len(lista)):
    if lista[i][1] == 'Sol':
        lista[i][1] = 1
    elif lista[i][1] == 'Nubes':
        lista[i][1] = 2
    elif lista[i][1] == 'Lluvia':
        lista[i][1] = 3
for e in lista:
    print(e)

print()
print(lista[1][0])
#print(lista[0])
#print(lista[1][1])