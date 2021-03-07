n = int(input())
stops = []
inside = 0
for i in range(n):
    stops.append(input())
maks = 0
for i in range(n):
    a,b = stops[i].split(" ")
    a,b = int(a), int(b)
    inside += b-a
    if maks < inside:
        maks = inside
    
print(maks)


