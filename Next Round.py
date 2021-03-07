temp = input()
n,k = temp.split(" ")
n = int(n)
k = int(k)
real_list = []
true = 0
if n >= k:
    temp = input()
    list = temp.split(" ")
    
for i in list:
    real_list.append(int(i))
del list



for i in range(n-1):
    for j in range(i+1,n):
         if real_list[i] < real_list[j]:
             temp = real_list[i]
             real_list[i] = real_list[j]
             real_list[j] = temp

for i in real_list:
    if i == 0:
        continue
    if i >= real_list[k-1]:
        true+=1

print(true)