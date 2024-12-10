filename = "input.txt"
# filename = "example.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append([-1]+[int(x) for x in line]+[-1])
		line = f.readline().strip()

grid = ([[-1]*len(grid[0])])+grid+([[-1]*len(grid[0])])

def reachable_peaks(xy, grid, cache={}):
	# if(depth>10):return 0
	peaks = set()
	height = grid[xy[1]][xy[0]]
	# print(xy, height, (xy in cache))
	if height == 9: 
		peaks.add(xy)
		return peaks
	if xy in cache: return cache[xy]
	if grid[xy[1]+1][xy[0]] == height+1:
		peaks = peaks.union(reachable_peaks((xy[0], xy[1]+1), grid, cache))
	if grid[xy[1]-1][xy[0]] == height+1:
		peaks = peaks.union(reachable_peaks((xy[0], xy[1]-1), grid, cache))
	if grid[xy[1]][xy[0]+1] == height+1:
		peaks = peaks.union(reachable_peaks((xy[0]+1, xy[1]), grid, cache))
	if grid[xy[1]][xy[0]-1] == height+1:
		peaks = peaks.union(reachable_peaks((xy[0]-1, xy[1]), grid, cache))
	cache[xy] = peaks
	return peaks

total = 0
for y,row in enumerate(grid):
	for x,v in enumerate(row):
		if(v==0):
			peaks = reachable_peaks((x,y), grid, {}) 
			# print((x,y), len(peaks))
			total+=len(peaks)
print(total)
