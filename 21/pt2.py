filename = "input.txt"
# filename = "example.txt"

keypads = [
	# 789
	# 456
	# 123
	# _0A
	"789456123 0A",
	# _^A
	# <v>
	" ^A<v>"
]

numeric_paths = {}
directional_paths = {}

def routes(a,b,pad):
	startposition = pad.index(a)
	pos = startposition
	blankpos = pad.index(" ")
	endpos = pad.index(b)
	# 2 possible routes: horiz then vert., and vert. then horiz.
	# a route is invalid if it passes over the blank

	blank_in_hv = (blankpos // 3 == startposition // 3) and (blankpos % 3 == endpos % 3)
	blank_in_vh = (blankpos % 3 == startposition % 3) and (blankpos // 3 == endpos // 3)
	# h->v
	out = set()
	if not blank_in_hv:
		orders = ""
		while endpos % 3 > pos % 3:
			orders += ">"
			pos += 1
		while endpos % 3 < pos % 3:
			orders += "<"
			pos -= 1
		while endpos // 3 > pos // 3:
			orders += "v"
			pos += 3
		while endpos // 3 < pos // 3:
			orders += "^"
			pos -= 3
		orders += "A"
		out.add(orders)
	# v-> h
	pos = startposition
	if not blank_in_vh:
		orders = ""
		while endpos // 3 > pos // 3:
			orders += "v"
			pos += 3
		while endpos // 3 < pos // 3:
			orders += "^"
			pos -= 3
		while endpos % 3 > pos % 3:
			orders += ">"
			pos += 1
		while endpos % 3 < pos % 3:
			orders += "<"
			pos -= 1
		orders += "A"
		out.add(orders)
	out = list(out)
	# out.sort()
	return out

for start in keypads[0]:
	for end in keypads[0]:
		paths = routes(start, end, keypads[0])
		# print(start, end, paths)
		numeric_paths[(start, end)] = paths

for start in keypads[1]:
	for end in keypads[1]:
		paths = routes(start, end, keypads[1])
		# print(start, end, paths)
		directional_paths[(start, end)] = paths

def next_layer(path, paths):
	nl = [""]
	prev = "A"
	for p in path:
		opts = paths[(prev, p)]
		# print("{} -> {} = {}".format(prev, p, opts))
		new = []
		if(len(opts) == 1):
			for i,v in enumerate(nl):
				nl[i] = v+opts[0]
		else:
			for i,v in enumerate(nl):
				nl[i] = v+opts[0]
				new.append(v+opts[1])
			nl = nl + new
		prev = p
	# print (nl)
	return nl

minimal_dir_paths = {}
costs = {}
for start in keypads[1]:
	for end in keypads[1]:
		rs = directional_paths[(start, end)]
		min_option = ""
		minlen = float('inf')
		minpath = ""
		minr = ""
		for r in rs:
			paths = next_layer(r, directional_paths)
			for p in paths:
				if len(p) < minlen:
					minpath = p
					minlen = len(p)
					minr = r
		minimal_dir_paths[(start, end)] = minr
		# print(start, end, minlen, minr)
		costs[(start, end, 0)] = 1
		costs[(start, end, 1)] = len(minr)

def movecost(start, end, layer):
	global costs
	# A> on l0 = 1 - just press >
	# A> on l1 = vA = 2
	# A> on l2 = c(Av,l1)+1+c(vA,l1)+1
		# Av on l1 = v<A = 3
		# vA on l1 = >^A = 3
	k = (start, end, layer)
	if k in costs: return costs[k]
	minpathcost = float('inf')
	for p in directional_paths[(start, end)]:
		m = seqcost(p, layer-1)
		if m<minpathcost:
			minpathcost=m
	cost = minpathcost
	costs[k] = cost
	return cost

def seqcost(sequence, layer):
	# assume cursor starts at A
	sequence = "A"+sequence
	prev = sequence[0]
	cost = 0
	for i in range(1,len(sequence)):
		cost += movecost(sequence[i-1], sequence[i], layer)
	return cost

# print("C",minimal_dir_paths[(' ','>')])
# print("D0",movecost('A','<',0))
# print("D1",movecost('A','<',1))
# print("D2",movecost('A','<',2))
# print("D3",movecost('A','<',3))
# print("D4",movecost('A','<',4))
# print("E",seqcost('<A^A>^^AvvvA',0))
# print("E",seqcost('<A^A>^^AvvvA',1))
# for k in costs.keys():
# 	if(k[2] == 1):
# 		print("{} -> {}: {} {}".format(k[0],k[1],minimal_dir_paths[(k[0],k[1])], costs[k]))

# seq = 'AAAAAA<'
# print("E0",seqcost(seq,0))
# print("E1",seqcost(seq,1))
# print("E2",seqcost(seq,2))
# print("E3",seqcost(seq,3))
# print("E4",seqcost(seq,4))
# print("E5",seqcost(seq,5))
# print("E6",seqcost(seq,6))
# print(costs[("A","<",3)])
# print(costs[("<","A",3)])
# <A^A>^^AvvvA
LAYERS = 2
LAYERS = 25
total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		solution = line
		# convert numeric code to directional
		solutions = next_layer(solution, numeric_paths)
		solutions = [seqcost(x, LAYERS) for x in solutions]
		mul = int(line[:-1])
		total += mul*min(solutions)
		line = f.readline().strip()

# Initially i thought there was an "always correct" route from 
# key X to key Y, where all high order keypads would result
# in less keypresses. Mentally I can't really think of why this
# isnt true, since every higher order sequence should start and end
# at A... Some edge case scenario maybe. But once I figured out
# I should just cache the results of keypresses 1 layer up
# AND try each possible route from key X to key Y (Since there are
# only ever 2 distinct routes), it was solvable.

# Used some hints from reddit just to ensure I was on the right track
# Easily the hardest puzzle of the year so far, probably took me 4+ hours
print(total)