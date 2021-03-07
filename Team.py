n = int(input())
liste = [[None]*3]*n
true = 0
confirmation = 0
for i in range(n):
    temp = input()
    liste[i][0], liste[i][1], liste[i][2] = temp.split(" ")
    if liste[i][0] == '1':
        confirmation += 1

    if liste[i][1] == '1':
        confirmation += 1

    if liste[i][2] == '1':
        confirmation += 1

    if confirmation >= 2:
        true += 1
    
    confirmation = 0
print(true)


