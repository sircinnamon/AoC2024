filename = "input.txt"
# filename = "example.txt"

frequencies = {}
grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()

for y, row in enumerate(grid):
	for x, v in enumerate(row):
		if(v != '.'):
			if(v in frequencies):
				frequencies[v].append((x,y))
			else:
				frequencies[v] = [(x,y)]
# print(frequencies)

def dist(xy_a, xy_b):
	return (xy_b[0]-xy_a[0], xy_b[1]-xy_a[1])

def in_bounds(xy, grid_dimensions):
	if(xy[0] < 0 or xy[0]>=grid_dimensions[0]): return False
	if(xy[1] < 0 or xy[1]>=grid_dimensions[1]): return False
	return True

antinodes = set()
grid_size = (len(grid[0]), len(grid))
for freq in frequencies:
	ants = frequencies[freq]
	for i, ant_a in enumerate(ants):
		antinodes.add(ant_a)
		for ant_b in ants[i+1:]:
			diff = dist(ant_a, ant_b)
			mult = 2
			while(in_bounds((ant_a[0]+diff[0]*mult, ant_a[1]+diff[1]*mult), grid_size)):
				antinodes.add((ant_a[0]+diff[0]*mult, ant_a[1]+diff[1]*mult))
				mult+=1
			mult = -1
			while(in_bounds((ant_a[0]+diff[0]*mult, ant_a[1]+diff[1]*mult), grid_size)):
				antinodes.add((ant_a[0]+diff[0]*mult, ant_a[1]+diff[1]*mult))
				mult-=1
print(len(antinodes))

# for y, row in enumerate(grid):
# 	for x, v in enumerate(row):
# 		if(v=='.' and (x,y) in antinodes):
# 			print('#', end='')
# 		else:
# 			print(v,end='')
# 	print('')