from tkinter.filedialog import askopenfilename, asksaveasfile
import re

readfile = askopenfilename()
writefile = asksaveasfile()

with open("new_store_d.txt", "a", encoding="utf-8") as new_file:
    file = open(readfile, "r", encoding="utf-8")
    lines = file.readlines()

    pattern = "-NID.+"

    for ln in lines:
        if "\"title\"" in ln and "NID" in ln:
            tmp = re.sub(pattern, '\"', ln)
            print(ln)
            print(tmp)
        #     new_file.write(tmp)
        # else:
        #     new_file.write(ln)

    file.close()
