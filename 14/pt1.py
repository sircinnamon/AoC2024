import re
filename = "input.txt"
# filename = "example.txt"

grid_size = (101,103)
# grid_size = (11,7)
time = 100
quadrants = [0,0,0,0]

def predict_robot_pos(start, vector, time):
	global grid_size
	end_pos = (
		(start[0]+(vector[0]*time))%grid_size[0],
		(start[1]+(vector[1]*time))%grid_size[1]
	)
	return end_pos

def pos_to_quadrant(pos):
	global grid_size
	if pos[0]>(grid_size[0]-1)//2:
		if pos[1]>(grid_size[1]-1)//2:
			return 3
		elif pos[1]<(grid_size[1]-1)//2:
			return 1
	elif pos[0]<(grid_size[0]-1)//2:
		if pos[1]>(grid_size[1]-1)//2:
			return 2
		elif pos[1]<(grid_size[1]-1)//2:
			return 0
	return -1

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		# p=67,43 v=80,86
		m = re.match(r'^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$', line)
		robot = ((int(m[1]),int(m[2])), (int(m[3]), int(m[4])))
		end_pos = predict_robot_pos(robot[0], robot[1], time)
		quad = pos_to_quadrant(end_pos)
		if(quad >= 0): quadrants[quad] = quadrants[quad]+1
		line = f.readline().strip()
print(quadrants)
print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])
