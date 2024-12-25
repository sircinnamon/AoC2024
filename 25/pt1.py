filename = "input.txt"
# filename = "example.txt"

keys = []
locks = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		typ = "key"
		if(line[0] == "#"):
			typ = "lock"
		sums = [0,0,0,0,0]
		line = f.readline().strip()
		for i in range(5):
			for j in range(len(sums)):
				if line[j] == "#": sums[j]+=1
			line = f.readline().strip()
		if typ == "key": keys.append(sums)
		else: locks.append(sums)
		line = f.readline().strip()
		line = f.readline().strip()
# print(keys)
# print(locks)
total = 0
locksize = 5
for k in keys:
	for l in locks:
		fits = True
		for i in range(len(k)):
			if(k[i] + l[i] > locksize):
				fits = False
				break
		if fits: total+=1
print(total)