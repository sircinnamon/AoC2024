filename = "input.txt"
# filename = "example.txt"

safecount = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		report = list(map(lambda x: int(x), line.split(" ")))
		# print(report)
		diffs = []
		for i in range(1,len(report)):
			diffs.append(report[i-1]-report[i])
		# print(" {}".format(diffs))
		safe = True
		if max(diffs) > 3:
			safe = False
		if min(diffs) < -3:
			safe = False
		if 0 in diffs:
			safe = False
		if max(diffs) > 0 and min(diffs) < 0:
			safe = False
		if(safe): safecount+=1
		line = f.readline().strip()
print(safecount)