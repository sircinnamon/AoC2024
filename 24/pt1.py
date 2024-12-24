import re
from collections import deque
filename = "input.txt"
# filename = "example.txt"

wires = {}
unsolved = deque()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		k,v = line.split(': ')
		wires[k] = int(v)
		line = f.readline().strip()
	line = f.readline().strip()
	while line:
		match = re.match(r'(.+) (.+) (.+) -> (.+)', line)
		unsolved.append((match[4], match[1], match[2], match[3]))
		line = f.readline().strip()

# print(wires)
# print(unsolved)
while len(unsolved) > 0:
	for u in unsolved:
		if u[1] in wires and u[3] in wires:
			if u[2] == "AND":
				wires[u[0]] = wires[u[1]] & wires[u[3]]
			elif u[2] == "OR":
				wires[u[0]] = wires[u[1]] | wires[u[3]]
			elif u[2] == "XOR":
				wires[u[0]] = wires[u[1]] ^ wires[u[3]]
			unsolved.remove(u)
			break
	# print(wires)
	# print(unsolved)
zs = list(filter(lambda x: x[0]=='z', wires.keys()))
zs.sort(reverse=True)
out = 0
for z in zs:
	out = out << 1
	out = out | wires[z]
	# print(wires[z], out)
print(out)