temp = input()

numbers = temp.split("+")

for i in range(len(numbers)):
    for j in range(len(numbers)-i-1):
        if int(numbers[j]) > int(numbers[j+1]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

value = None
i=0
while(i !=  len(numbers)-1):

    if value == None:
        value = numbers[i] + "+"
    else:
        value += numbers[i] + "+"

    i+=1
else:
    if value == None:
        value = numbers[i]
    else:
        value += numbers[i]
print(value)






