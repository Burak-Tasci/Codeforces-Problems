karpuz = int(input())
a = None
for i in range(karpuz):
    for j in range(karpuz):
        if (i + j) == karpuz:
            if i % 2 == 0 and j % 2 == 0:
                print("YES")
                a = 1
                break
    if a == 1:
        break
if a == None:
    print("NO")
      



