# n = int(input())
n = "090234"
# n.split()

a = int(n[0]) + int(n[1]) + int(n[2])
b = int(n[3]) + int(n[4]) + int(n[5])

if a == b:
    print("Счастливый")
else:
    print("Обычный")
