liste = []

for i in range(5):
    temp = input()
    liste.append(temp)

for i in range(len(liste)):
    if '1' in liste[i]:
        row = i+1
        break

columns = liste[row-1].split(" ")

for i in range(len(columns)):
    if '1' == columns[i]:
        column = i+1
        break


value = abs(row-3) + abs(column-3)
print(value)

