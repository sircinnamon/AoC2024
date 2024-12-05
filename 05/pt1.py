import math
filename = "input.txt"
# filename = "example.txt"

rules = {}
total = 0

def score(order, rules):
	for i in range(len(order)):
		r = rules[order[i]]
		for j in range(i):
			antirule = '{}|{}'.format(order[i], order[j])
			if antirule in r: return 0
	return order[math.floor(len(order)/2)]

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		ks = [int(x) for x in line.split("|")]
		if(ks[0] in rules): rules[ks[0]].append(line)
		else: rules[ks[0]] = [line]
		if(ks[1] in rules): rules[ks[1]].append(line)
		else: rules[ks[1]] = [line]
		line = f.readline().strip()

	# prints
	line = f.readline().strip()
	while line:
		order = [int(x) for x in line.split(",")]
		total += score(order, rules)
		line = f.readline().strip()

print(total)