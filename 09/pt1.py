filename = "input.txt"
# filename = "example.txt"

VERBOSE = False
def printv(*args, **kwargs):
	if(VERBOSE):print(*args, **kwargs)

data = ""
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		data = line	
		line = f.readline().strip()

data = [int(x) for x in data]
total = 0
fwd_ind = 0
bkwd_ind = len(data)-1
output_ind = 0
while fwd_ind < bkwd_ind:
	# file
	file_size = data[fwd_ind]
	file_id = fwd_ind//2
	for i in range(file_size):
		total += output_ind * file_id
		printv(file_id, end='-')
		output_ind += 1
	fwd_ind += 1
	# gap
	gap_size = data[fwd_ind]
	move_file_size = data[bkwd_ind]
	file_id = bkwd_ind//2
	for i in range(gap_size):
		while(move_file_size == 0) and bkwd_ind > fwd_ind:
			bkwd_ind -= 2
			file_id = bkwd_ind//2
			move_file_size = data[bkwd_ind]
		if(bkwd_ind <= fwd_ind):
			# consumed all backwards files and reached gap
			break
		total += output_ind * file_id
		printv(file_id, end='_')
		output_ind += 1
		move_file_size -= 1
		data[bkwd_ind] = data[bkwd_ind]-1
	fwd_ind+=1
if(fwd_ind == bkwd_ind):
	for i in range(data[fwd_ind]):
		total += (fwd_ind//2)*output_ind
		output_ind+=1
		printv(fwd_ind//2, end='+')
	printv("\n", fwd_ind, bkwd_ind)
printv("")
# not 6385073321180
# not 6385337128964
print(total)