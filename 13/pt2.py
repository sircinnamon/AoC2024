import re
import math
filename = "input.txt"
# filename = "example.txt"


def solve_machine(prize, a, b):
	offset = 10000000000000
	# offset = 0
	prize=(offset+prize[0], offset+prize[1])

	# Define a line where X = number of a presses
	# where where the x position will be a multiple of b's x value below the prize
	c_x = prize[0]/b[0]
	slope_x = (a[0]/b[0])*-1 # x*slope +c_x = y

	# Define a line where X = number of a presses
	# where where the y position will be a multiple of b's y value below the prize
	c_y = prize[1]/b[1]
	slope_y = (a[1]/b[1])*-1

	# The intersection of the two lines is how many A presses are needed
	# If it is a whole number, the game is "solvable"
	denom = b[0]*b[1]
	intersect_x = (c_x*denom - c_y*denom) / (slope_y*denom-slope_x*denom)

	# Floating point really does a number on this logic
	# If I could perfectly test if the result was an int, this test is unneeded
	# But the fastest way to check a valid answer is just to round it off and try it
	b_presses = (prize[0]-(intersect_x*a[0]))/b[0]
	tar_x = round(intersect_x)*a[0] + round(b_presses)*b[0]
	tar_y = round(intersect_x)*a[1] + round(b_presses)*b[1]
	# print((tar_x, tar_y), prize)
	if tar_x == prize[0] and tar_y == prize[1]:
		return (3*round(intersect_x) + round(b_presses))
	return 0


total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		a = re.match(r'^Button A: X\+(\d+), Y\+(\d+)', line)
		a = (int(a[1]), int(a[2]))
		line = f.readline().strip()
		b = re.match(r'^Button B: X\+(\d+), Y\+(\d+)', line)
		b = (int(b[1]), int(b[2]))
		line = f.readline().strip()
		prize = re.match(r'^Prize: X=(\d+), Y=(\d+)', line)
		prize = (int(prize[1]), int(prize[2]))
		# print(a, b, prize)
		req_tokens = solve_machine(prize, a, b)
		# print("\t", req_tokens)
		total += req_tokens
		line = f.readline().strip()
		line = f.readline().strip()

print(total)