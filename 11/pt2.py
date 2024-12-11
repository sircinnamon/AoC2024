import math
filename = "input.txt"
# filename = "example.txt"

stones = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		stones = [int(x) for x in line.split()]
		line = f.readline().strip()

def process_blinks(stone, blinks, cache):
	if(blinks == 0): return 1

	stone_count = 0
	if((stone, blinks) in cache):
		return cache[(stone, blinks)]
	ss = str(stone)
	if(stone == 0):
		stone_count = process_blinks(1, blinks-1, cache)
	elif(len(ss) % 2 == 0):
		h = len(ss)//2
		l_count_1 = process_blinks(int(ss[h:]), blinks-1, cache)
		l_count_2 = process_blinks(int(ss[:h]), blinks-1, cache)
		stone_count = l_count_1 + l_count_2
	else:
		stone_count = process_blinks(stone*2024, blinks-1, cache)
	cache[(stone, blinks)] = stone_count
	return stone_count

stone_count = 0
BLINKS = 75
cache = {}
# print("RUNNING FOR {} BLINKS".format(BLINKS))
for s in stones:
	# print(s)
	stone_count += process_blinks(s, BLINKS, cache)
print(stone_count)
# print(cache)