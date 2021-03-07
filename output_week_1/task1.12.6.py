# n = int(input())
n = 111

if n == 0 or n % 10 in (5, 6, 7, 8, 9, 0) or n % 100 in (11, 12, 13, 14):
    print(n, "программистов")
elif n % 10 in (2, 3, 4):
    print(n, "программиста")
else:
    print(n, "программист")
