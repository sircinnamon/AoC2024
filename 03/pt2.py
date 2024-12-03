import re
filename = "input.txt"
# filename = "example2.txt"

muls = []
with open(filename, "r") as f:
	line = f.readline().strip()
	body = ""
	while line:
		body += line.replace("\n", "")
		line = f.readline().strip()
	body = re.sub(r'don\'t\(\).*?(do\(\)|$)', '', body)
	muls = muls + re.findall(r'mul\(\d+,\d+\)', body)
# print(muls)
total = 0
for m in muls:
	match = re.search(r'mul\((\d+),(\d+)\)', m)
	v1 = match[1]
	v2 = match[2] 
	total += (int(v1)*int(v2))
print(total)