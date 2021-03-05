import re

with open("new_file", "a") as new_file:
    file = open("store_d.txt", "r")
    lines = file.readlines()

    pattern = "-NID.+"

    new_db = []
    for ln in lines:
        if "title" and "NID" in ln:
            tmp = re.sub(pattern, '', ln)
            new_file.write(tmp)
        else:
            new_file.write(ln)

    file.close()