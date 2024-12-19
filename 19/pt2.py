filename = "input.txt"
# filename = "example.txt"

towels = set()
solved = {}
longest_pattern = 0
def pattern_solutions(pattern, depth=0):
	if pattern in solved: return solved[pattern] # cache solved substrings
	solution_count = 0
	if pattern in towels: solution_count+=1
	for i in range(min(longest_pattern, len(pattern)-1)):
		substr = pattern[:i+1]
		if substr in towels:
			# print("\t{}: substr {} in pattern {}".format(depth, substr, pattern))
			subsolutions = pattern_solutions(pattern[i+1:], depth+1)
			solution_count += subsolutions
	# print("Final count for {}: {}".format(pattern, solution_count))
	solved[pattern] = solution_count
	return solution_count

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
		counter += pattern_solutions(line)
		# print("{} -> {}".format(line, solved[line]))
		line = f.readline().strip()
print(counter)