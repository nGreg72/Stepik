import re

file = open("store_d.txt", "r+")
lines = file.readlines()

pattern = "-NID.+"

for ln in lines :
    if "title" and "NID" in ln:
        re.sub(pattern, '', ln)
        print(ln)

file.close()
