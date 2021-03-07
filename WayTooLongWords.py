n = int(input())
list = []
for i in range(n):
    word = input()
    if (len(word) <= 10):
        list.append(word)
        pass
    else:
        list.append("{}{}{}".format(word[0],str(len(word)-2),word[-1]))

for i in range(n):
    print(list[i])
