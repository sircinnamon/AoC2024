filename = "input.txt"
# filename = "example.txt"

moveset = {
	"^": (0,-1),
	">": (+1,0),
	"v": (0,+1),
	"<": (-1,0)
}

def move_entity(pos, grid, move):
	# Assume move has been validated with entity_can_move
	entity = grid[pos[1]][pos[0]]
	next_pos = (pos[0]+move[0], pos[1]+move[1])
	if entity == ".": return next_pos # Do nothing, will be destroyed
	if entity == "#":
		print("ERROR: Tried to move a wall")
		return False
	if entity == "@":
		move_entity(next_pos, grid, move) # move anything out of the way
		grid[next_pos[1]][next_pos[0]] = "@"
		grid[pos[1]][pos[0]] = "."
		return next_pos
	if entity == "[":
		if(move[0] == 1):
			# Moving left side of box into right side of box
			move_entity((next_pos[0]+1, next_pos[1]), grid, move)
		else:
			move_entity(next_pos, grid, move) # move anything out of the way
		if(move[1] != 0):
			move_entity((next_pos[0]+1, next_pos[1]), grid, move) # move anything out of the way
		# Move both sides
		grid[pos[1]][pos[0]] = "."
		grid[pos[1]][pos[0]+1] = "."
		grid[next_pos[1]][next_pos[0]] = "["
		grid[next_pos[1]][next_pos[0]+1] = "]"
		return next_pos
	if entity == "]":
		# Move by the left side
		move_entity((pos[0]-1, pos[1]), grid, move)
		return next_pos

def entity_can_move(pos, grid, move):
	entity = grid[pos[1]][pos[0]]
	if entity == ".":
		return True # Empty space can move out of the way of objects
	if entity == "#":
		return False # Wall will never move
	if entity == "@":
		# can the robot move?
		desired_pos = (pos[0]+move[0], pos[1]+move[1])
		return entity_can_move(desired_pos, grid, move)
	if entity == "[":
		# can a left-side box move?
		# check for 2 clear spaces when moving up/down
		if move[1] != 0:
			desired_pos_a = (pos[0]+move[0], pos[1]+move[1])
			desired_pos_b = (pos[0]+move[0]+1, pos[1]+move[1])
			return entity_can_move(desired_pos_a, grid, move) and entity_can_move(desired_pos_b, grid, move)
		else:
			desired_pos = (pos[0]+move[0], pos[1]+move[1])
			return entity_can_move(desired_pos, grid, move)
	if entity == "]":
		# can a right-side box move?
		# check for 2 clear spaces when moving up/down
		if move[1] != 0:
			desired_pos_a = (pos[0]+move[0], pos[1]+move[1])
			desired_pos_b = (pos[0]+move[0]-1, pos[1]+move[1])
			return entity_can_move(desired_pos_a, grid, move) and entity_can_move(desired_pos_b, grid, move)
		else:
			desired_pos = (pos[0]+move[0], pos[1]+move[1])
			return entity_can_move(desired_pos, grid, move)

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
			if(v=="["):
				score += 100*y + x
	return score

grid = []
moves = []
robot = (0,0)
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		line = line.replace("#", "##")
		line = line.replace(".", "..")
		line = line.replace("O", "[]")
		line = line.replace("@", "@.")
		if "@" in line:
			robot = (line.index("@"), len(grid))
		grid.append(list(line))
		line = f.readline().strip()
	line = f.readline().strip()
	# print_grid(robot, grid)
	while line:
		for m in line:
			m = moveset[m]
			valid_move = entity_can_move(robot, grid, m)
			# print("VALID MOVE {}: {}".format(m, valid_move))
			if(valid_move): robot = move_entity(robot, grid, m)
			# print_grid(robot, grid)
		line = f.readline().strip()

# print_grid(robot, grid)
print(score_grid(grid))