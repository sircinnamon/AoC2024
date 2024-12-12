from collections import deque
filename = "input.txt"
# filename = "example.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()

grid_size = (len(grid[0]), len(grid)) #xy

def build_zone(start, grid):
	# Walk through adjacent and add to set if they match
	grid_size = (len(grid[0]), len(grid)) #xy
	queue = deque([
		(start[0]+1, start[1]),
		(start[0]-1, start[1]),
		(start[0], start[1]+1),
		(start[0], start[1]-1),
	])
	v = grid[start[1]][start[0]]
	zone = set([start])
	while len(queue) > 0:
		curr = queue.popleft()
		if(curr in zone): continue
		if(curr[0] < 0 or curr[0] >= grid_size[0]): continue
		if(curr[1] < 0 or curr[1] >= grid_size[1]): continue
		if(grid[curr[1]][curr[0]] != v): continue
		# print("({}, {}) = {}".format(curr[0], curr[1], grid[curr[1]][curr[0]]))
		zone.add(curr)
		queue.append((curr[0]+1, curr[1]))
		queue.append((curr[0]-1, curr[1]))
		queue.append((curr[0], curr[1]+1))
		queue.append((curr[0], curr[1]-1))
	return zone

def calculate_zone_corners(zone):
	corners = 0
	for t in zone:
		# Create a bool for if each surrounding tile is "in zone""
		N = ((t[0], t[1]-1) in zone)
		E = ((t[0]+1, t[1]) in zone)
		S = ((t[0], t[1]+1) in zone)
		W = ((t[0]-1, t[1]) in zone)
		NE = ((t[0]+1, t[1]-1) in zone)
		SE = ((t[0]+1, t[1]+1) in zone)
		NW = ((t[0]-1, t[1]-1) in zone)
		SW = ((t[0]-1, t[1]+1) in zone)
		# A tile may qualify as a corner in multiple ways
		# single nodes (no adjacent)
		if(not N and not E and not S and not W): corners+=4
		# pokey nodes (touches zone on just 1 side)
		if(N and not E and not S and not W): corners+=2
		if(E and not S and not W and not N): corners+=2
		if(S and not W and not N and not E): corners+=2
		if(W and not N and not E and not S): corners+=2
		# convex corners
		if(S and E and not N and not W): corners+=1
		if(S and W and not N and not E): corners+=1
		if(N and E and not S and not W): corners+=1
		if(N and W and not S and not E): corners+=1
		# concave corners
		if(E and N and not NE): corners+=1
		if(E and S and not SE): corners+=1
		if(W and N and not NW): corners+=1
		if(W and S and not SW): corners+=1

	return corners

checked = set()
total = 0
for y,row in enumerate(grid):
	for x,v in enumerate(row):
		start = (x,y)
		if (x,y) in checked: continue
		# print(start)
		zone = build_zone(start, grid)
		area = len(zone)
		corners = calculate_zone_corners(zone)
		total += area*corners
		# print("Start {} v:{} area:{} corners:{}".format(start, grid[start[1]][start[0]], area, corners))
		checked = checked.union(zone)
print(total)