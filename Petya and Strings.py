first = input()
second = input()

first , second= first.lower(), second.lower()
value = 0

if len(first)  <= len(second):
    for i in range(len(first)):
        if first[i] < second[i]:
            value = -1
            break
        elif first[i] > second[i]:
            value = 1
            break

else:
    for i in range(len(second)):
        if first[i] < second[i]:
            value = -1
            break
        elif first[i] > second[i]:
            value = 1
            break

print(value)

