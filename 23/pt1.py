filename = "input.txt"
# filename = "example.txt"

computers = {}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		cp1, cp2 = line.split("-")
		if cp1 not in computers:
			computers[cp1] = set()
		if cp2 not in computers:
			computers[cp2] = set()
		computers[cp1].add(cp2)
		computers[cp2].add(cp1)
		line = f.readline().strip()

triples = set()
for k in computers.keys():
	if k.startswith('t'):
		# print("{} peers {}".format(k, computers[k]))
		for peer in computers[k]:
			copeers = computers[peer].intersection(computers[k])
			if len(copeers) > 0:
				# print("triplet members {} {} {}".format(k, peer, copeers))
				for cp in copeers:
					sortd = [k, peer, cp]
					sortd.sort()
					triples.add((sortd[0],sortd[1],sortd[2]))
# print(triples)
print(len(triples))