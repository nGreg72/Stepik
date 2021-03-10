pattern = "(-NID\d+-\d+)"

# def startRename():
#     directory = f"{os.getcwd()}\\"
#     directory1 = directory.replace('/', '\\')
#     files = os.listdir(directory)
#
#     for file in files:
#         os.rename(directory1 + file, directory1 + file.replace('Без названия', ''))
#
# startRename()

baseDir = 'C:/temp/'
# bd = filter(os.path.isdir, os.listdir(baseDir))

# directories = filter(os.path.isdir, os.listdir(baseDir))
#
# print("CurDir : ", os.path.isdir(baseDir))
#
# for d in directories:
#     print("AAA", baseDir)

# for ls in os.listdir(baseDir):
#     # print(baseDir + ls)
#     if os.path.isdir(baseDir + ls):
#         print(baseDir + ls)


import hashlib
import subprocess
#
# def md5checksum(fname):
#
#     md5 = hashlib.md5()
#
#     f = open(fname, "rb")
#
#     while chunk := f.read(4096):
#         md5.update(chunk)
#
#         return md5.hexdigest()
#
# result = md5checksum("C:/Users/nGreg\Dropbox/PycharmProjects/Stepik/output_week_1/fixDB.py")
# print(result)

with open("C:/Users/nGreg\Dropbox/PycharmProjects/Stepik/output_week_1/fixDB.py", "rb") as f:
    md5 = hashlib.md5(f.read())
print(md5.hexdigest())

programm = "C:/Users/nGreg/Dropbox/PycharmProjects/Stepik/md5sum.exe"
argument = "C:/Users/nGreg/Dropbox/PycharmProjects/Stepik/output_week_1/store_d.txt"
subprocess.call([programm, argument])
