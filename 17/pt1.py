import math
filename = "input.txt"
# filename = "example.txt"

program = []
A = 0
B = 0
C = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	A = int(line.split(" ")[-1])
	line = f.readline().strip()
	B = int(line.split(" ")[-1])
	line = f.readline().strip()
	C = int(line.split(" ")[-1])
	line = f.readline().strip()
	line = f.readline().strip()
	program = [int(x) for x in line.split(" ")[1].split(',')]
print(A,B,C)
print(program)

def combo(x):
	if x==0 or x==1 or x==2 or x==3:
		return x
	if x == 4:
		return A
	if x == 5:
		return B
	if x == 6:
		return C
	if x == 7:
		print("ERROR")

pointer = 0
out = []
while pointer < len(program):
	opcode = program[pointer]
	operand = program[pointer+1]
	jumped = False
	if opcode == 0:
		# adv
		A = math.floor(A / 2**combo(operand))
	if opcode == 1:
		# bxl
		B = B ^ operand
	if opcode == 2:
		# bst
		B = combo(operand) % 8
	if opcode == 3:
		# jnz
		if A == 0:
			pass
		else:
			jumped = True
			pointer = operand
	if opcode == 4:
		# bxc
		B = B ^ C
	if opcode == 5:
		# out
		out.append(str(combo(operand)%8))
	if opcode == 6:
		# adv
		B = math.floor(A / 2**combo(operand))
	if opcode == 7:
		# adv
		C = math.floor(A / 2**combo(operand))
	if not jumped:
		pointer += 2

print(",".join(out))