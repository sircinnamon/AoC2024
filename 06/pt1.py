filename = "input.txt"
# filename = "example.txt"

grid = []
N = (0,-1)
E = (+1,0)
S = (0,+1)
W = (-1,0)
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line.replace(".", " "))
		line = f.readline().strip()

guard = ((0,0), N) #x, y, facing
obstacles = []
for y, row in enumerate(grid):
	for x, v in enumerate(row): 
		if v == "^":
			guard = ((x,y), N)
		if v == "#":
			obstacles.append((x,y))

visited = set()
while (guard[0][0] in range(0, len(grid[0]))) and (guard[0][1] in range(0, len(grid))):
	pos = guard[0]
	visited.add(pos)
	next_pos = (pos[0]+guard[1][0], pos[1]+guard[1][1])
	if next_pos in obstacles:
		# turn
		next_facing = E if guard[1] == N else S if guard[1] == E else W if guard[1] == S else N
		guard = (pos, next_facing)
	else:
		guard = (next_pos, guard[1])

# print(visited)
print(len(visited))