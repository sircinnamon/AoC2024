import re
import math
filename = "input.txt"
# filename = "example.txt"

grid_size = (101,103)
# grid_size = (11,7)
grid_center = grid_size[0]-1//2

def predict_robot_pos(start, vector, time):
	global grid_size
	end_pos = (
		(start[0]+(vector[0]*time))%grid_size[0],
		(start[1]+(vector[1]*time))%grid_size[1]
	)
	return end_pos

def treelike(robots, time):
	# is the arrangement at time "treelike"
	global grid_size
	global grid_center
	# look for a low std deviation in x and y
	# admittedly I got this idea from reddit
	# but in my defense, I didnt know what
	# the "picture of a christmas tree" looked like
	positions = list(map(lambda r: predict_robot_pos(r[0], r[1], time), robots))
	avg_x = sum([p[0] for p in positions]) / len(robots)
	avg_y = sum([p[1] for p in positions]) / len(robots)
	# print("avg_x {} avg_y {}".format(avg_x, avg_y))
	variance_x = [(p[0]-avg_x)**2 for p in positions]
	variance_y = [(p[1]-avg_y)**2 for p in positions]
	std_dev_x = math.sqrt(sum(variance_x)/len(variance_x))
	std_dev_y = math.sqrt(sum(variance_y)/len(variance_y))
	# print("std_dev_x {} std_dev_y {}".format(std_dev_x, std_dev_y))
	return (std_dev_x < 20) and (std_dev_y < 20)

def to_string(robots, t):
	global grid_size
	grid = [[' ']*grid_size[0] for i in range(grid_size[1])]
	for r in robots:
		pos = predict_robot_pos(r[0], r[1], t)
		grid[pos[1]][pos[0]] = "#"
	return "\n".join(["".join(row) for row in grid])

robots = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		# p=67,43 v=80,86
		m = re.match(r'^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$', line)
		robot = ((int(m[1]),int(m[2])), (int(m[3]), int(m[4])))
		robots.append(robot)
		line = f.readline().strip()

t = 0
while True:
	if(treelike(robots, t)):
		print(to_string(robots, t))
		print(t)
		break
	t+=1