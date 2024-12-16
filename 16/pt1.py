from collections import deque
filename = "input.txt"
# filename = "example.txt"

grid = []
start = (0,0)
end = (0,0)
scores = {}
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
			end = (line.index("E"), len(grid)-1)
		line = f.readline().strip()
# print(start)
# print(end)
scores[start] = 0

to_check = deque([start])
while len(to_check) > 0:
	#current = x,y,facing (N,E,S,W)
	current = to_check.popleft()
	# print(current)
	curr_score = scores[current]
	# go straight
	nxt = (current[0]+moveset[current[2]][0], current[1]+moveset[current[2]][1], current[2])
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

print(min([
	scores[(end[0],end[1],"N")],
	scores[(end[0],end[1],"E")],
	scores[(end[0],end[1],"S")],
	scores[(end[0],end[1],"W")]
]))