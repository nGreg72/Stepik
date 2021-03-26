a = int(input())
b = int(input())

range_a = range(1, a * b + 1)

for i in range_a:
    if i % a == 0 and i % b == 0:
        print(i)
        break
