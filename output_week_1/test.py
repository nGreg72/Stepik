import os

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

for ls in os.listdir(baseDir):
    # print(baseDir + ls)
    if os.path.isdir(baseDir + ls):
        print(baseDir + ls)
