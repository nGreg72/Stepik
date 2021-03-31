a = int(input('a:'))
b = int(input('b:'))

lst = [i for i in range(a, b + 1) if i % 3 == 0]

tmp = 0

for i in lst:
    tmp += i

result = tmp / len(lst)
print(result)
