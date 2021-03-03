file = open("store_d.txt", "r")
lines = file.readlines()

for ln in lines:
    print(ln)

file.close()
