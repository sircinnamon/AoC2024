import re
filename = "input.txt"
filename = "example.txt"

grid = []
pattern = r'XMAS'
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()
count = 0

# horizontal
for row in grid:
	count += len(re.findall(pattern, row))
	count += len(re.findall(pattern, row[::-1]))

# vertical
rotated = ["".join([x[i] for x in grid]) for i in range(len(grid))]
for col in rotated:
	count += len(re.findall(pattern, col))
	count += len(re.findall(pattern, col[::-1]))

diag_asc = []
diag_desc = []
for s in range(len(grid)+len(grid[0])-1):
	y_asc = min(s, len(grid)-1)
	x_asc = s - y_asc
	row_asc = ""+grid[y_asc][x_asc]
	while(y_asc > 0 and x_asc < len(grid[0])-1):
		x_asc+=1
		y_asc-=1
		row_asc+=grid[y_asc][x_asc]
	diag_asc.append(row_asc)

	x_desc = max(0, len(grid[0])-s-1)
	y_desc = max(0, s-(len(grid[0])-1))
	row_desc = ""+grid[y_desc][x_desc]
	while(y_desc < len(grid)-1 and x_desc > 0):
		x_desc-=1
		y_desc+=1
		row_desc+=grid[y_desc][x_desc]
	diag_desc.append(row_desc)

for stripe in diag_asc:
	count += len(re.findall(pattern, stripe))
	count += len(re.findall(pattern, stripe[::-1]))

for stripe in diag_desc:
	count += len(re.findall(pattern, stripe))
	count += len(re.findall(pattern, stripe[::-1]))

print(count)
