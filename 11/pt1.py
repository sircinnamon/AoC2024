filename = "input.txt"
# filename = "example.txt"

stones = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		stones = [int(x) for x in line.split()]
		line = f.readline().strip()

def process_blinks(stones, blinks):
	if(blinks == 0): return len(stones)

	stone_count = 0
	for s in stones:
		ss = str(s)
		if(s == 0):
			stone_count += process_blinks([1], blinks-1)
		elif(len(ss) % 2 == 0):
			h = len(ss)//2
			stone_count += process_blinks([int(ss[h:]), int(ss[:h])], blinks-1)
		else:
			stone_count += process_blinks([s*2024], blinks-1)
	return stone_count

stone_count = 0
BLINKS = 25
for s in stones:
	stone_count += process_blinks([s], BLINKS)
print(stone_count)