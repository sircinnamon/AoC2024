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

antinodes = set()
for y in range(len(grid)):
	for x in range(len(grid[0])):
		for freq in frequencies:
			if((x,y) in antinodes): break
			ants = frequencies[freq]
			for i, ant_a in enumerate(ants):
				for ant_b in ants[i+1:]:
					dist_a = dist((x,y), ant_a)
					dist_b = dist((x,y), ant_b)
					if(2*dist_a[0]==dist_b[0] and 2*dist_a[1]==dist_b[1]):
						antinodes.add((x,y))
						# print((x,y), freq, ant_a, ant_b, dist_a, dist_b)
					elif(2*dist_b[0]==dist_a[0] and 2*dist_b[1]==dist_a[1]):
						antinodes.add((x,y))
						# print((x,y), freq, ant_a, ant_b, dist_a, dist_b)
print(len(antinodes))

# for y, row in enumerate(grid):
# 	for x, v in enumerate(row):
# 		if(v=='.' and (x,y) in antinodes):
# 			print('#', end='')
# 		else:
# 			print(v,end='')
# 	print('')