# x = float(input())
# y = float(input())
# z = input()

x = 5.0
y = 10.0
z = "/"

if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "/" and y != 0:
    print(x / y)
elif z == "*":
    print(x * y)
elif z == "mod" and y != 0:
    print(x % y)
elif z == "pow":
    print(pow(x, y))
elif z == "div" and y != 0:
    print(x // y)
else:
    print("Деление на 0!")

