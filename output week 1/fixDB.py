import re

file = open("store_d.txt", "r+", encoding="utf-8")
lines = file.readlines()

pattern = "-NID.+"

x = []

for ln in lines :
    if "title" and "NID" in ln:
        w = re.sub(pattern, '', ln)
        x.append(w)
        # print(w)

file.close()

print(x)