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
            print(ln)
            print(tmp)
        #     new_file.write(tmp)
        # else:
        #     new_file.write(ln)

    file.close()

def md5checksum(fname):

    md5 = hashlib.md5()

    f = open(fname, "rb")

    while chunk := f.read(4096):
        md5.update(chunk)

        return md5.hexdigest()

result = md5checksum(readfile)
print(result)
