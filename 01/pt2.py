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
digit_count = {}
score = 0
for v in list_r:
	if(v in digit_count):
		digit_count[v] += 1
	else:
		digit_count[v] = 1

for v in list_l:
	if(v in digit_count):
		score+= digit_count[v]*v
print(score)
