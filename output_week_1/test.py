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

with open("C:/Users/nGreg/Dropbox/PycharmProjects/Stepik/output_week_1/store_d.txt", 'rb') as file:
    a = file.read()
    b = hashlib.md5(a).hexdigest()
print(b)

# def file_as_bytes(file):
#     with file:
#         return file.read()
# print(hashlib.md5(file_as_bytes(open("C:/Users/nGreg/Dropbox/PycharmProjects/Stepik/output_week_1/store_d.txt", 'rb'))).hexdigest())

