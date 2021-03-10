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


def file_as_bytes(file):
    with file:
        return file.read()

hash_summ = hashlib.md5(file_as_bytes(open("C:/Users/nGreg/Dropbox/PycharmProjects/Stepik/output_week_1/store_d.txt", 'rb'))).hexdigest()

with open(writefile + ".md5", "w") as new_md:
    new_md.write(hash_summ)
