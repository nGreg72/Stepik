A = 2000

if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
    print("Високосный год")
else:
    print("Обычный")