A = int(input("A"))
B = int(input("B"))
H = int(input("H"))

if A <= H <= B:
    print("Это нормально")
elif H > B:
    print("Пересып")
elif H < A:
    print("Недосып")