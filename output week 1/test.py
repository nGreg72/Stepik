a = [i for i in range(1001)]

for i in a:
    i = str(i)
    if i.split(i[-1]) == 2:
        print(i)