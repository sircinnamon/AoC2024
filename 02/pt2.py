filename = "input.txt"
# filename = "example.txt"

def isSafe(report):
	diffs = []
	for i in range(1,len(report)):
		diffs.append(report[i-1]-report[i])
	safe = True
	if max(diffs) > 3:
		safe = False
	if min(diffs) < -3:
		safe = False
	if 0 in diffs:
		safe = False
	if max(diffs) > 0 and min(diffs) < 0:
		safe = False
	return safe

safecount = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		report = list(map(lambda x: int(x), line.split(" ")))
		# print(report)
		# print(" {}".format(diffs))
		if(isSafe(report)):
			safecount+=1
		else:
			# try removing one at a time
			for i in range(len(report)):
				subreport = report[:i]+report[i+1:]
				if(isSafe(subreport)):
					safecount+=1
					break
		line = f.readline().strip()
print(safecount)