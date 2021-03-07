n = int(input())
colours = input()
value = 0
for i in range(len(colours)):
    try:
        if colours[i] == colours[i+1]:
            value+=1
    except IndexError:
        pass
print(value)

