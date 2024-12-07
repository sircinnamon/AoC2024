filename = "input.txt"
# filename = "example.txt"

def solvable(value, target, operands):
	# print("v:{} t:{} o:{}".format(value, target, operands))
	if(len(operands) == 0):
		return value == target
	# Addition
	new_value = value + operands[0]
	if(new_value<=target):
		if(solvable(new_value, target, operands[1:])):
			return True

	# Multiplication
	new_value = value * operands[0]
	if(new_value<=target):
		if(solvable(new_value, target, operands[1:])):
			return True
	return False

total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		target = int(line.split(":")[0])
		operands = [int(x) for x in line.split(" ")[1:]]
		if(solvable(operands[0], target, operands[1:])):
			total += target
			# print(target)
		line = f.readline().strip()
print(total)