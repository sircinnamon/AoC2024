filename = "input.txt"
# filename = "example.txt"

grid = []
N = (0,-1)
E = (+1,0)
S = (0,+1)
W = (-1,0)

def check_route_for_loops(guard, obstacles, prev_visited):
	visited = prev_visited.copy() # include facing
	while (guard[0][0] in range(0, len(grid[0]))) and (guard[0][1] in range(0, len(grid))):
		pos = guard[0]
		if(guard in visited):
			# looping
			return True
		visited.add(guard)
		next_pos = (pos[0]+guard[1][0], pos[1]+guard[1][1])
		while next_pos not in obstacles:
			pos = next_pos
			next_pos = (next_pos[0]+guard[1][0], next_pos[1]+guard[1][1])
			if(next_pos[0] not in range(len(grid[0]))):
				return False
			if(next_pos[1] not in range(len(grid))):
				return False
		# turn
		next_facing = E if guard[1] == N else S if guard[1] == E else W if guard[1] == S else N
		guard = (pos, next_facing)
	return False

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

loop_creators = set()
visited = set()
starting_pos = guard
i = 0
while (guard[0][0] in range(0, len(grid[0]))) and (guard[0][1] in range(0, len(grid))):
	i+=1
	if(i%100==0):print(i)
	pos = guard[0]
	next_pos = (pos[0]+guard[1][0], pos[1]+guard[1][1])
	# test an obstacle at next pos
	test_obs = obstacles[:] + [next_pos]
	if(next_pos not in loop_creators):
		if(check_route_for_loops(starting_pos, test_obs, visited)):
			loop_creators.add(next_pos)
	if next_pos in obstacles:
		# turn
		next_facing = E if guard[1] == N else S if guard[1] == E else W if guard[1] == S else N
		guard = (pos, next_facing)
	else:
		guard = (next_pos, guard[1])

print(loop_creators)
print(len(loop_creators))