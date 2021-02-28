# a = int(input())

base_word = "программист"
x = "а"
y = "ов"

gen = list(range(1000))
c = 22

if c == 1:
    print(base_word)
elif 2 <= c <= 4:
    print(base_word + x)
elif 5 <= c <= 9 or c == 0:
    print(base_word + y)

print(gen)

"""if month == 1:
    template = re.sub(r"month", "год", template)
elif (month >= 2 and month <= 4) :
    template = re.sub(r"\bmonth\b", "года", template)
elif (month >= 5):
    template = re.sub(r"\bmonth\b", "лет", template)"""