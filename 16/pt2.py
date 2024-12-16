from collections import deque
filename = "input.txt"
# filename = "example.txt"

grid = []
start = (0,0)
ends = []
scores = {}
antiscores = {}
moveset = {
	"N": (0,-1),
	"E": (+1,0),
	"S": (0,+1),
	"W": (-1,0)
}
turns = {
	"N": "EW",
	"E": "NS",
	"S": "EW",
	"W": "NS"
}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(list(line))
		if "S" in line:
			start = (line.index("S"), len(grid)-1, "E")
		if "E" in line:
			ends.append((line.index("E"), len(grid)-1, "N"))
			ends.append((line.index("E"), len(grid)-1, "E"))
			ends.append((line.index("E"), len(grid)-1, "S"))
			ends.append((line.index("E"), len(grid)-1, "W"))
		line = f.readline().strip()
# print(start)
# print(end)

def calculate_distances(scores, to_check, invert=False):
	global grid
	current = to_check.popleft()
	# print(current)
	curr_score = scores[current]
	# go straight
	nxt = (current[0]+moveset[current[2]][0], current[1]+moveset[current[2]][1], current[2])
	if invert:
		nxt = (current[0]-moveset[current[2]][0], current[1]-moveset[current[2]][1], current[2])
	if(grid[nxt[1]][nxt[0]] == "#"):
		pass # it's a wall, cant move there
	elif(nxt not in scores or scores[nxt] > curr_score+1):
		scores[nxt] = curr_score+1
		to_check.append(nxt)

	# turns
	nxt_a = (current[0], current[1], turns[current[2]][0])
	nxt_b = (current[0], current[1], turns[current[2]][1])
	if(nxt_a not in scores or scores[nxt_a] > curr_score+1000):
			scores[nxt_a] = curr_score+1000
			to_check.append(nxt_a)
	if(nxt_b not in scores or scores[nxt_b] > curr_score+1000):
			scores[nxt_b] = curr_score+1000
			to_check.append(nxt_b)

scores[start] = 0
antiscores[ends[0]] = 0
antiscores[ends[1]] = 0
antiscores[ends[2]] = 0
antiscores[ends[3]] = 0

to_check = deque([start])
while len(to_check) > 0:
	calculate_distances(scores, to_check)

# to find all valid paths, get distance from end, and for each
# point, check if dist(start)+dist(end) = best case
to_check = deque(ends)
while len(to_check) > 0:
	calculate_distances(antiscores, to_check, invert=True)

best = min([
	scores[ends[0]],
	scores[ends[1]],
	scores[ends[2]],
	scores[ends[3]],
])
count = 0

for y in range(len(grid)):
	for x in range(len(grid[0])):
		for d in moveset.keys():
			pt = (x,y,d)
			if(pt not in scores or pt not in antiscores): continue
			score = scores[pt]
			antiscore = antiscores[pt]
			if(score+antiscore == best):
				count += 1
				break # dont double count directions
print(count)