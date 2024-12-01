import re

filename = "input.txt"
# filename = "example.txt"

list_l = list()
list_r = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		a, b = re.split(r'\s+', line)
		list_l.append(int(a))
		list_r.append(int(b))
		line = f.readline().strip()

list_l.sort()
list_r.sort()
dist = 0
for i in range(len(list_l)):
	dist += abs(list_l[i] - list_r[i])

print(dist)
