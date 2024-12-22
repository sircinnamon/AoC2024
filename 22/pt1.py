filename = "input.txt"
# filename = "example.txt"

def next_secret_number(s):
	mod = 16777216
	s = ((s<<6)^s) # * 64
	s = s % mod
	s = ((s>>5)^s) # // 32
	s = s % mod
	s = ((s<<11)^s) # * 2048
	s = s % mod
	return s

total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		s = int(line)
		for i in range(2000):
			s = next_secret_number(s)
		# print(line, '->', s)
		total+=s
		line = f.readline().strip()
print(total)