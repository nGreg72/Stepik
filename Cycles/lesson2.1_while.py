# a = 5
#
# while a > 0:
#     print(a, end="")  # end для того, чтобы не переводить курсор на новую строку
#     a -= 1


# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

"""Вычисление суммы целых чисел на отрезке от A до B"""
sum = 0
a = 3
b = 7
i = a   # counter

while i <= b:
    sum += i
    i += 1
print(sum)
