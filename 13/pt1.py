import re
filename = "input.txt"
# filename = "example.txt"


def solve_machine(prize, a, b):
	start_factor = min((prize[0]//b[0])+1, 100)
	presses = (0, start_factor)
	while presses[1]>0 or presses[0]<100:
		current_pos = (
			a[0]*presses[0]+b[0]*presses[1],
			a[1]*presses[0]+b[1]*presses[1]
		)
		# print(presses, current_pos)
		if(current_pos == prize): break
		if(current_pos[0] > prize[0] and presses[1]>0):
			# un-press B
			presses = (presses[0], presses[1]-1)
		else:
			# press A
			presses = (presses[0]+1, presses[1])
	current_pos = (a[0]*presses[0]+b[0]*presses[1],a[1]*presses[0]+b[1]*presses[1])
	if(current_pos == prize):
		return presses[0]*3 + presses[1]
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