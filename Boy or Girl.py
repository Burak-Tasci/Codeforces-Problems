username = input().lower()

username = set(username)

n = len(username)

if n % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")

