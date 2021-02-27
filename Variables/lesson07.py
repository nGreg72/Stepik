X = int(input("X ="))
H = int(input("H ="))
M = int(input("M ="))

h = H * 60  #60
current_time = h + M  # 115
full_time = current_time + X # 590

h = full_time // 60  # 9
tmp_m = h * 60  # 540
m = full_time - tmp_m

print(h)
print(m)
