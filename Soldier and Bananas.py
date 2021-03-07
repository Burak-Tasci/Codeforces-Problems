temp = input()
k,n,w = temp.split(" ")
sum = 0
k,n,w = int(k), int(n), int(w)
for i in range(1,w+1):
    sum += i*k

if sum-n > 0:
    print(sum-n)
else:
    print("0")