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
data = [(i//2 if i%2==0 else 0, x) for i,x in enumerate(data)]
data.append((0,0))
total = 0
bkwd_ind = len(data)-2
printv(data)
checked_file_id = data[bkwd_ind][0]+1
while bkwd_ind>0:
	move_file_size = data[bkwd_ind][1]
	move_file_id = data[bkwd_ind][0]

	# A file necessarily CANNOT move twice
	# (It is already in the leftmost gap that it could fit in)
	# But save time by nto double checking
	if(move_file_id > checked_file_id):
		bkwd_ind-=2
		continue
	else:
		checked_file_id = move_file_id
	printv("Checking fileid {} (ind:{})".format(move_file_id, bkwd_ind))
	gap_index = 1
	while(data[gap_index][1] < move_file_size):
		gap_index+=2
		if(gap_index >= bkwd_ind): break
	if(gap_index < bkwd_ind):
		remaining_gap = data[gap_index][1] - move_file_size
		created_gap = (0, data[bkwd_ind-1][1]+move_file_size+data[bkwd_ind+1][1])
		# data = data[:bkwd_ind-1]+[created_gap]+data[bkwd_ind+2:]
		# data = data[:gap_index]+[(0,0),(move_file_id, move_file_size),(0,remaining_gap)]+data[gap_index+1:]
		# Insert file with a 0 gap before and a gap of remaining size after
		# place a merged gap of pregap+filesize+postgap where file was
		data = data[:gap_index]+\
				[(0,0),(move_file_id, move_file_size),(0,remaining_gap)]+\
				data[gap_index+1:bkwd_ind-1]+\
				[created_gap]+\
				data[bkwd_ind+2:]
		printv("fileid {} moved to gap at {}".format(move_file_id, gap_index))
		bkwd_ind += 2
	printv(data)
	bkwd_ind-=2

printv(data)
total = 0
output_ind = 0
for i,f in enumerate(data):
	for _ in range(f[1]):
		total += f[0]*output_ind
		output_ind += 1
		if(f[0] == 0 and i != 0):
			printv(".", end='')
		else:
			printv(f[0], end='')

printv("")
# not 9894339190945
print(total)