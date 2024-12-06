filename = "input.txt"
# filename = "example.txt"

grid = []
N = (0,-1)
E = (+1,0)
S = (0,+1)
W = (-1,0)

def check_route_for_loops(guard, grid):
	gx = guard[0][0]
	gy = guard[0][1]
	gdx = guard[1][0]
	gdy = guard[1][1]
	minx = 0
	maxx = len(grid[0])
	miny = 0
	maxy = len(grid)
	visited = set() # include facing
	while (gx >= minx) and (gx < maxx) and (gy >= minx) and (gy < maxy):
		if((gx, gy, gdx, gdy) in visited):
			# looping
			return True
		visited.add((gx, gy, gdx, gdy))
		count = 1
		nxx = gx + gdx*count
		nxy = gy + gdy*count
		while grid[nxy][nxx] != '#':
			count += 1
			nxx = gx + gdx*count
			nxy = gy + gdy*count
			if(nxx < minx) or (nxx >= maxx) or (nxy < minx) or (nxy >= maxy):
				return False
		nxx = nxx - gdx #backstep from obstacle
		nxy = nxy - gdy #backstep from obstacle
		# turn
		next_facing = E if (gdx, gdy) == N else S if (gdx, gdy) == E else W if (gdx, gdy) == S else N
		gdx = next_facing[0]
		gdy = next_facing[1]
		gx = nxx
		gy = nxy
	return False

def ghost_grid(grid, x, y):
	newgrid = [row[:] for row in grid][:]
	newgrid[y] = newgrid[y][:x]+"#"+newgrid[y][x+1:]
	return newgrid

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line.replace(".", "_"))
		line = f.readline().strip()

guard = ((0,0), N) #x, y, facing
for y, row in enumerate(grid):
	for x, v in enumerate(row): 
		if v == "^":
			guard = ((x,y), N)

loop_creators = set()
starting_pos = guard
i = 0
while True:
	# i+=1
	# if(i%100==0):print(i)
	pos = guard[0]
	next_pos = (pos[0]+guard[1][0], pos[1]+guard[1][1])
	# test an obstacle at next pos
	if next_pos[0] >= len(grid[0]) or next_pos[1] >= len(grid):
		break
	if next_pos[0] < 0 or next_pos[1] < 0:
		break
	test_grid = ghost_grid(grid, next_pos[0], next_pos[1])
	if(next_pos not in loop_creators):
		if(check_route_for_loops(starting_pos, test_grid)):
			loop_creators.add(next_pos)
	if grid[next_pos[1]][next_pos[0]] == "#":
		# turn
		next_facing = E if guard[1] == N else S if guard[1] == E else W if guard[1] == S else N
		guard = (pos, next_facing)
	else:
		guard = (next_pos, guard[1])

# print(loop_creators)
print(len(loop_creators))