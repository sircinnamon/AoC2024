filename = "input.txt"
# filename = "example.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()
count = 0

def check_match(xy, grid):
	dirs = [
		(-1,-1),(+1,-1),
		(-1,+1),(+1,+1),
	]
	if(xy[0] <= 0 or xy[0] >= len(grid[0])-1): return 0
	if(xy[1] <= 0 or xy[1] >= len(grid)-1): return 0
	corners = list(map(lambda d: grid[xy[1]+d[1]][xy[0]+d[0]], dirs))
	if(corners[0] != 'S' and corners[0] != 'M'):return 0
	if(corners[1] != 'S' and corners[1] != 'M'):return 0
	if(corners[2] != 'S' and corners[2] != 'M'):return 0
	if(corners[3] != 'S' and corners[3] != 'M'):return 0
	if(corners[0] == corners[3]): return 0
	if(corners[1] == corners[2]): return 0
	return 1
for i, row in enumerate(grid):
	for j in range(len(row)):
		if (row[j] == 'A'):
			count += check_match((j,i), grid)
print(count)
