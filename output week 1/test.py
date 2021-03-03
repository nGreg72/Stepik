import os

# def startRename():
#     directory = f"{os.getcwd()}\\"
#     directory1 = directory.replace('/', '\\')
#     files = os.listdir(directory)
#
#     for file in files:
#         os.rename(directory1 + file, directory1 + file.replace('Без названия', ''))
#
# startRename()

baseDir = 'C:/Temp/'
# bd = filter(os.path.isdir, os.listdir(baseDir))

directories = filter(os.path.isdir, os.listdir(baseDir))
for d in directories:
    print(d)

# for ls in directories:

    # if os.path.isdir(fn):
    #     print()
        # continue
    # else:
