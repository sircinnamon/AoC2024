filename = "input.txt"
# filename = "example.txt"

towels = set()
solved = set()
longest_pattern = 0
def is_pattern_solvable(pattern, depth=0):
	if pattern in towels: return True
	if pattern in solved: return True # cache solved substrings
	for i in range(min(longest_pattern, len(pattern)-1)):
		substr = pattern[:i+1]
		if substr in towels:
			# print("{}: substr {} in pattern {}".format(depth, substr, pattern))
			if(is_pattern_solvable(pattern[i+1:], depth+1)):
				solved.add(pattern)
				return True
	return False

counter = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	towels = set(line.split(", "))
	longest_pattern = max([len(x) for x in line.split(", ")])
	line = f.readline().strip()
	line = f.readline().strip()
	# print(towels)
	# print(longest_pattern)
	while line:
		if(is_pattern_solvable(line)):
			counter += 1
		line = f.readline().strip()
print(counter)