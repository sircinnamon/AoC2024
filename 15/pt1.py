filename = "input.txt"
# filename = "example.txt"

def move_robot(pos, grid, move):
	moveset = {
		"^": (0,-1),
		">": (+1,0),
		"v": (0,+1),
		"<": (-1,0)
	}
	move = moveset[move]
	next_pos = (pos[0]+move[0], pos[1]+move[1])
	move_items = 1
	while grid[next_pos[1]][next_pos[0]] != ".":
		if(grid[next_pos[1]][next_pos[0]] == "#"):
			# hit wall, cant move
			return pos
		if(grid[next_pos[1]][next_pos[0]] == "O"):
			# hit box
			move_items+=1
			next_pos = (next_pos[0]+move[0], next_pos[1]+move[1])
	# move is valid
	for i in range(move_items,0,-1):
		curr = (pos[0]+(move[0]*i), pos[1]+(move[1]*i))
		nxt = (pos[0]+(move[0]*(i-1)), pos[1]+(move[1]*(i-1)))
		# print("PUT {} AT {},{}".format(grid[nxt[1]][nxt[0]], curr[0], curr[1]))
		grid[curr[1]][curr[0]] = grid[nxt[1]][nxt[0]]
	grid[pos[1]][pos[0]] = "."


	return (pos[0]+move[0], pos[1]+move[1])

def print_grid(pos, grid):
	for y,row in enumerate(grid):
		if(pos[1] == y):
			row_s = "".join(row)
			row_s = row_s[:pos[0]]+"@"+row_s[pos[0]+1:]
			print(row_s)
		else:
			print("".join(row))

def score_grid(grid):
	score = 0
	for y,row in enumerate(grid):
		for x,v in enumerate(row):
			if(v=="O"):
				score += 100*y + x
	return score

grid = []
moves = []
robot = (0,0)
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		if "@" in line:
			robot = (line.index("@"), len(grid))
			line = line.replace("@", ".")
		grid.append(list(line))
		line = f.readline().strip()
	line = f.readline().strip()
	while line:
		for m in line:
			robot = move_robot(robot, grid, m)
			# print("MOVED ",m)
			# print_grid(robot, grid)
		line = f.readline().strip()

# print_grid(robot, grid)
print(score_grid(grid))