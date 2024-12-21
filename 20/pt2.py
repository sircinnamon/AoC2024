from collections import deque
filename = "input.txt"
# filename = "example.txt"
# filename = "tmp.txt"

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
total = 0
for pt in dist.keys():
	# try and cheat to every other point on the path
	for xmod in range(-20,21):
		for ymod in range((20-abs(xmod))*-1, (21-abs(xmod))):
			cheat = (pt[0]+xmod,pt[1]+ymod)
			if(cheat not in dist):continue
			if(dist[cheat][0]<dist[pt][0]):continue
			jump = abs(pt[0]-cheat[0]) + abs(pt[1]-cheat[1])
			if jump <= 20 and dist[cheat][0]>(dist[pt][0]+jump):
				saved = dist[cheat][0]-(dist[pt][0]+jump)
				if(saved >= 100):total+=1
			# print("Cheat from {} to {} saves {}".format(pt, cheat, saved))

print(total)