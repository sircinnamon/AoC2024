import math
filename = "input.txt"
# filename = "example.txt"

rules = {}
total = 0

def score(order, rules, depth=0):
	# print(depth)
	for i in range(len(order)):
		r = rules[order[i]]
		for j in range(i):
			antirule = '{}|{}'.format(order[i], order[j])
			if antirule in r:
				new_order = order[::1]
				new_order[i] = order[j]
				new_order[j] = order[i]
				return score(new_order, rules, depth+1) 
	if(depth==0): return 0
	else: return order[math.floor(len(order)/2)]

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