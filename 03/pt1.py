import re
filename = "input.txt"
# filename = "example.txt"

muls = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		muls = muls + re.findall(r'mul\(\d+,\d+\)', line)
		line = f.readline().strip()
# print(muls)
total = 0
for m in muls:
	match = re.search(r'mul\((\d+),(\d+)\)', m)
	v1 = match[1]
	v2 = match[2] 
	total += (int(v1)*int(v2))
print(total)