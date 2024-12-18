from collections import deque
filename = "input.txt"
# filename = "example.txt"

grid_size = 70
# grid_size = 6
grid = [["."]*(grid_size+1) for i in range(grid_size+1)]
blocks = []
dirs = [(0,+1),(0,-1),(+1,0),(-1,0)]
# print(grid)
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		x,y = [int(x) for x in line.split(",")]
		blocks.append((x,y))
		line = f.readline().strip()


def printgrid(grid):
	for y,row in enumerate(grid):
		for x,v in enumerate(row):
			print(v, end='')
		print('')

TIME = 1024
# TIME = 12
for i in range(TIME):
	x,y = blocks[i]
	grid[y][x] = "#"

dist = {}
dist[(0,0)] = 0
to_check = deque([(0,0)])
# printgrid(grid)
while len(to_check) > 0:
	curr = to_check.popleft()
	for d in dirs:
		nxt = (curr[0]+d[0], curr[1]+d[1])
		if(nxt[0] < 0 or nxt[0] > grid_size): continue
		if(nxt[1] < 0 or nxt[1] > grid_size): continue
		if(grid[curr[1]][curr[0]] == "#"): continue
		nxt_score = dist[curr] + 1
		if(nxt not in dist or dist[nxt] > nxt_score):
			dist[nxt] = nxt_score
			to_check.append(nxt)
# print(dist)
print(dist[(grid_size, grid_size)])
