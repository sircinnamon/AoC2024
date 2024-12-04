filename = "input.txt"
# filename = "example.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()
count = 0

def count_match(xy, grid):
	# 8 cardinal directions
	dirs = [
		(-1,-1), (0,-1), (+1,-1),
		(-1, 0), (+1, 0),
		(-1,+1), (0,+1), (+1,+1),
	]
	match = "XMAS"
	count = 0
	for d in dirs:
		if(grid[xy[1]][xy[0]] != match[0]):continue
		if(xy[0]+(3*d[0]) < 0):continue
		if(xy[0]+(3*d[0]) >= len(grid[0])):continue
		if(xy[1]+(3*d[1]) < 0):continue
		if(xy[1]+(3*d[1]) >= len(grid)):continue
		if(grid[xy[1]+d[1]*1][xy[0]+d[0]*1] != match[1]):continue
		if(grid[xy[1]+d[1]*2][xy[0]+d[0]*2] != match[2]):continue
		if(grid[xy[1]+d[1]*3][xy[0]+d[0]*3] != match[3]):continue
		count+=1
	# if(count>0):
	# 	print(xy, count)
	return count
for i, row in enumerate(grid):
	for j in range(len(row)):
		if (row[j] == 'X'):
			count += count_match((j,i), grid)
print(count)
