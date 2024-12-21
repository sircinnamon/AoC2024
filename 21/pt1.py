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
	return list(out)

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


total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		minlen=99999
		# print("=== {} ===".format(line))
		l2s = next_layer(line, numeric_paths)
		for l2 in l2s:
			# print(l2)
			l3s = next_layer(l2, directional_paths)
			for l3 in l3s:
				# print(l3)
				l4s = next_layer(l3, directional_paths)
				for l4 in l4s:
					minlen = min(minlen, len(l4))
			# print(l4)
		mul = int(line[:-1])
		# print(minlen)
		total += mul*minlen
		line = f.readline().strip()
print(total)