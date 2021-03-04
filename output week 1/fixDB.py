import re

title = "utro_YKT_140121-NID130770-4869434.avi"
title_lrv = "utro_YKT_140121-NID130770-4869434.11898/utro_YKT_140121-NID130770-4869434_lrv.avi"

file = open("store_d.txt", "r")
lines = file.readlines()

for ln in lines:
    print(ln)

file.close()
