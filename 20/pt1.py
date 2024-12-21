from collections import deque
filename = "input.txt"
# filename = "example.txt"

grid = []
start = (0,0)
end = (0,0)
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		if("S" in line):
			start = (line.index("S"), len(grid))
		if("E" in line):
			end = (line.index("E"), len(grid))
		grid.append(list(line))
		line = f.readline().strip()

def printgrid():
	for row in grid:
		print("".join(row))

# printgrid()
# print(start, end)
dist = {}
dist[start] = (0, start) # distance from start, origin node
to_check = deque([start])
# collect each node's distance from start
while len(to_check) > 0:
	curr = to_check.popleft()
	for d in dirs:
		nxt = (curr[0]+d[0], curr[1]+d[1])
		if grid[nxt[1]][nxt[0]] == "#":
			continue
		if nxt not in dist or dist[nxt][0] > dist[curr][0]+1:
			dist[nxt] = (dist[curr][0]+1, curr)
			to_check.append(nxt)

# distance to end
# print(dist[end])

# locate cheats
cheats = {}
for pt in dist.keys():
	# try and cheat in all 4 directions
	for d in dirs:
		cheat = (pt[0]+d[0]*2, pt[1]+d[1]*2)
		if(cheat in dist and dist[cheat][0] > (dist[pt][0]+2)):
			saved = dist[cheat][0]-(dist[pt][0]+2)
			if saved in cheats:
				cheats[saved].append((pt, cheat))
			else:
				cheats[saved] = [(pt,cheat)]
			# print("Cheat from {} to {} saves {}".format(pt, cheat, saved))

total = 0
for k in cheats.keys():
	# print("There are {} cheats that save {} picoseconds".format(len(cheats[k]), k))
	if(k>=100): total+=len(cheats[k])
print(total)