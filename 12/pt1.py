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

def calculate_zone_perimeter(zone):
	fence = 0
	for t in zone:
		if((t[0]+1, t[1]) not in zone): fence+=1
		if((t[0]-1, t[1]) not in zone): fence+=1
		if((t[0], t[1]+1) not in zone): fence+=1
		if((t[0], t[1]-1) not in zone): fence+=1
	return fence

checked = set()
total = 0
for y,row in enumerate(grid):
	for x,v in enumerate(row):
		start = (x,y)
		if (x,y) in checked: continue
		# print(start)
		zone = build_zone(start, grid)
		area = len(zone)
		perimeter = calculate_zone_perimeter(zone)
		total += area*perimeter
		checked = checked.union(zone)
print(total)