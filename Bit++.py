step = int(input())

value = 0
for i in range(step):
    temp = input()
    if "--" in temp:
        value -= 1
    elif "++" in temp:
        value += 1

print(value)