import hashlib
import re
from tkinter.filedialog import askopenfilename, asksaveasfilename

readfile = askopenfilename()
writefile = asksaveasfilename()

with open(writefile, "a", encoding="utf-8") as new_file:
    file = open(readfile, "r", encoding="utf-8")
    lines = file.readlines()

    pattern = "-NID.+"

    for ln in lines:
        if "\"title\"" in ln and "NID" in ln:
            tmp = re.sub(pattern, '\"', ln)
            # print(ln)
            # print(tmp)
            new_file.write(tmp)
        else:
            new_file.write(ln)

    file.close()

with open(writefile + ".md5", "w") as new_md:
    f = open(readfile, "rb")
    a = f.read()
    b = hashlib.md5(a).hexdigest()
    new_md.write(b)
