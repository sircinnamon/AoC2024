import math
filename = "input.txt"
# filename = "example.txt"

program = []
A = 0
A_reset = 0
B = 0
B_reset = 0
C = 0
C_reset = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	A = int(line.split(" ")[-1])
	A_reset = A
	line = f.readline().strip()
	B = int(line.split(" ")[-1])
	B_reset = B
	line = f.readline().strip()
	C = int(line.split(" ")[-1])
	C_reset = C
	line = f.readline().strip()
	line = f.readline().strip()
	program = [int(x) for x in line.split(" ")[1].split(',')]
# print(A,B,C)
# print(program)

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

def verify_output(current, desired):
	# current should be a suffix or exact match to desired
	if(len(current) > len(desired)):return False
	for i in range(1,len(current)+1):
		if(current[-i] != desired[-i]):return False
	return True

pointer = 0
out = []
# counter = 0 # checked up to 10000000
# base = 8**(len(program))
testval = 0
while True:
	# A = counter
	A = testval
	B = B_reset
	C = C_reset
	out = []
	pointer = 0
	# print(v, "===")
	while pointer < len(program):
		opcode = program[pointer]
		operand = program[pointer+1]
		# print("\t{:2}- {} {} [A:{} B:{} C:{}]".format(pointer,opcode,operand,A,B,C))
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
			out.append((combo(operand)%8))
		if opcode == 6:
			# adv
			B = math.floor(A / 2**combo(operand))
		if opcode == 7:
			# adv
			C = math.floor(A / 2**combo(operand))
		if not jumped:
			pointer += 2
	# print(out)
	if(verify_output(out, program)):
		# print("Matched {} digits".format(len(out)))
		if(len(out) == len(program)):
			break
		else:
			testval = 8*testval
	else:
		testval+=1

# This is obviously not a perfectly universal solution
# but I'm guessing all inputs are constructed with the 
# same property: each digit is only affected by the 
# certain "power of 8 multiple" related to that digit
# so multiplying starting A values by 8 will preserve
# the putput digits and add a new one in front
print(testval)