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

seqscores = {}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		s = int(line)
		seq = (None, None, None, None)
		prev_digit = s%10
		seen = set()
		for i in range(2000):
			s = next_secret_number(s)
			last_digit = s%10
			seq = (seq[1], seq[2], seq[3], last_digit - prev_digit)
			if(seq not in seen):
				if(seq in seqscores): seqscores[seq] += last_digit
				else: seqscores[seq] = last_digit
				seen.add(seq)
			prev_digit = last_digit
		# print(line, '->', s)
		line = f.readline().strip()
best = max(seqscores.values())
# for k in seqscores.keys():
# 	if seqscores[k]>=best:
# 		print("{} {}".format(k, seqscores[k]))
# print(seqscores)
print(best)
