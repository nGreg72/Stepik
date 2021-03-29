tmp = 0

while tmp == 0:
    a = int(input("Enter digit:"))

    if a < 10:
        continue
    if a > 100:
        break
    print(a)

