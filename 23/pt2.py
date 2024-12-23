filename = "input.txt"
# filename = "example.txt"

computers = {}
complete_subgraphs = {}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		cp1, cp2 = line.split("-")
		if cp1 not in computers:
			computers[cp1] = set([cp1])
		if cp2 not in computers:
			computers[cp2] = set([cp2])
		computers[cp1].add(cp2)
		computers[cp2].add(cp1)
		line = f.readline().strip()

def netstr(netset):
	s = list(netset)
	s.sort()
	return "-".join(s)

def build_complete_graph(comps):
	global computers
	global complete_subgraphs
	key = netstr(comps)
	if(key in complete_subgraphs): return complete_subgraphs[key]
	complist = list(comps)
	peers = []
	if(len(complist) > 0):
		peers = computers[complist[0]]
		for c in complist[1:]:
			peers = peers.intersection(computers[c])
		peers = peers.difference(comps)
	else:
		peers = set(computers.keys())
	# peers are new nodes adjacent to all allowed nodes
	# print("set {} has peers {}".format(comps, peers))
	if len(peers) == 0:
		return comps
	possibles = []
	for p in peers:
		poss = comps.copy()
		poss.add(p)
		possibles.append(poss)
	# print(possibles)
	grown_graphs = []
	for p in possibles:
		ng = build_complete_graph(p)
		if ng not in grown_graphs:
			grown_graphs.append(ng)
	longest_graph = []
	for ng in grown_graphs:
		if len(ng) > len(longest_graph):
			longest_graph = ng
	complete_subgraphs[key] = longest_graph
	return longest_graph

# Greedily try all subgraphs, depht first
# cache [subgraph] to [best complete graph it is a member of]
# largest subgraph containing the empty set is the winner
# sort and print
ln = list(build_complete_graph(set([])))
ln.sort()
# print(ln)
print(",".join(ln))
