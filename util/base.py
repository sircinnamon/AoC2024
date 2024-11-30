filename = "input.txt"
filename = "example.txt"

with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		
		line = f.readline().strip()