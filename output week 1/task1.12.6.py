# n = int(input())
n = 21

base_word = "программист"
x = "а"
y = "ов"

if n in (0, 5, 6, 7, 8, 9, 10) or n % 100 == 11:
    print(base_word + y)
elif not n % 100 == 11:
    print(base_word + x)
else:
    print(base_word)



"""if month == 1:
    template = re.sub(r"month", "год", template)
elif (month >= 2 and month <= 4) :
    template = re.sub(r"\bmonth\b", "года", template)
elif (month >= 5):
    template = re.sub(r"\bmonth\b", "лет", template)"""