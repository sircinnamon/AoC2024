import re
from collections import deque
filename = "input.txt"
# filename = "example.txt"

wires = {}
gates = {}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		k,v = line.split(': ')
		wires[k] = int(v)
		line = f.readline().strip()
	line = f.readline().strip()
	while line:
		match = re.match(r'(.+) (.+) (.+) -> (.+)', line)
		gates[match[4]] = (match[1],match[2],match[3])
		line = f.readline().strip()

def get_val(wires, reg):
	zs = list(filter(lambda x: x[0]==reg, wires.keys()))
	zs.sort(reverse=True)
	out = 0
	for z in zs:
		out = out << 1
		out = out | wires[z]
		# print(wires[z], out)
	return out

def set_val(wires, val, reg):
	zs = list(filter(lambda x: x[0]==reg, wires.keys()))
	zs.sort()
	for z in zs:
		wires[z] = val & 1
		# print("set wire {} to {}".format(z, val&1))
		val = val >> 1
		# print(wires[z], out)

def solve_system(wires, gates):
	# print(wires)
	# print(unsolved)
	tmp_wires = {}
	for w in wires.keys():
		tmp_wires[w] = wires[w]
	unsolved = deque()
	for g in gates.keys():
		if g not in tmp_wires: unsolved.append((g, gates[g][0], gates[g][1], gates[g][2]))
	while len(unsolved) > 0:
		for u in unsolved:
			if u[1] in tmp_wires and u[3] in tmp_wires:
				if u[2] == "AND":
					tmp_wires[u[0]] = tmp_wires[u[1]] & tmp_wires[u[3]]
				elif u[2] == "OR":
					tmp_wires[u[0]] = tmp_wires[u[1]] | tmp_wires[u[3]]
				elif u[2] == "XOR":
					tmp_wires[u[0]] = tmp_wires[u[1]] ^ tmp_wires[u[3]]
				unsolved.remove(u)
				break
		# print(tmp_wires)
		# print(unsolved)
	zs = list(filter(lambda x: x[0]=='z', tmp_wires.keys()))
	zs.sort(reverse=True)
	out = 0
	for z in zs:
		out = out << 1
		out = out | tmp_wires[z]
		# print(tmp_wires[z], out)
	return out

def get_ancestors(wires, reg):
	ancestors = set()
	to_check = deque([reg])
	while len(to_check) > 0:
		curr = to_check.popleft()
		if curr in gates:
			v1 = gates[curr][0]
			v2 = gates[curr][2]
			if v1 not in ancestors:
				ancestors.add(v1)
				to_check.append(v1)
			# else: print("DOUBLE ANC ",reg, v1)
			if v2 not in ancestors:
				ancestors.add(v2)
				to_check.append(v2)
			# else: print("DOUBLE ANC ",reg, v2)
	return ancestors

def xy_range(r):
	out = set()
	for i in range(r):
		x = 'x{:02}'.format(i)
		y = 'y{:02}'.format(i)
		out.add(x)
		out.add(y)
	return out

def traverse_gates(gates):
	gates_in = {}
	for g in gates.keys():
		ins = [gates[g][0], gates[g][2]]
		op = gates[g][1]
		out = g
		gates_in[(ins[0], ins[1], op)] = out
		gates_in[(ins[1], ins[0], op)] = out

	carry_gates = {}
	out_gate = gates_in[('x00', 'y00', "XOR")]
	carry_gates[0] = gates_in[('x00', 'y00', "AND")]
	for i in range(1,46):
		# print("{}..".format(i),end="")
		x = 'x{:02}'.format(i)
		y = 'y{:02}'.format(i)
		z = 'z{:02}'.format(i)
		a_gate = gates_in[(x, y, "XOR")]
		if(a_gate.startswith("z")):
			# print("BAD A GATE")
			break
		d_gate = gates_in[(x, y, "AND")]
		if(d_gate.startswith("z")):
			# print("BAD D GATE")
			swapped_d_gate = find_d_gate(gates_in, i)
			return set([swapped_d_gate, d_gate])
		carry_gate = carry_gates[i-1]
		if (a_gate, carry_gate, "XOR") not in gates_in:
			# print("NO B GATE FOR {}".format(i))
			# print("SHOULD BE {} = {}".format(z, gates[z]))
			# print("EXPECTED {} XOR {}".format(a_gate, carry_gate))
			return set([gates[z][0], gates[z][2]]).symmetric_difference(set([a_gate, carry_gate]))
		b_gate = gates_in[(a_gate, carry_gate, "XOR")]
		if (a_gate, carry_gate, "AND") not in gates_in:
			# print("NO C GATE FOR {}".format(i))
			break
		c_gate = gates_in[(a_gate, carry_gate, "AND")]
		if(c_gate.startswith("z")):
			# print("BAD C GATE")
			swapped_c_gate = find_c_gate(gates_in, i)
			return set([swapped_c_gate, c_gate])
		if (c_gate, d_gate, "OR") not in gates_in:
			# print("NO E GATE FOR {}".format(i))
			# print("EXPECTED {} OR {}".format(c_gate, d_gate))
			break
		e_gate = gates_in[(c_gate, d_gate, "OR")]
		out_gate = b_gate
		carry_gates[i] = e_gate
	return []


def find_a_gate(gates, i):
	x = 'x{:02}'.format(i)
	y = 'y{:02}'.format(i)
	a_gate = gates[(x, y, "XOR")]
	return a_gate

def find_d_gate(gates, i):
	a_gate = find_a_gate(gates, i)
	child_gates = list(filter(lambda x: x[0]==a_gate and x[2]=="AND", gates.keys()))
	c_gate = []
	if(len(child_gates) == 1):
		c_gate = child_gates[0]
	else:
		print("AMBIGUOUS C GATE")
	e_gate = []
	c_gate_value = gates[c_gate]
	child_gates = list(filter(lambda x: x[0]==c_gate_value and x[2]=="OR", gates.keys()))
	if(len(child_gates) == 1):
		e_gate = child_gates[0]
	else:
		print("AMBIGUOUS E GATE")
	if(e_gate[0] == c_gate_value): return e_gate[1]
	else: return e_gate[0]

def find_c_gate(gates, i):
	# a_gate = find_a_gate(gates, i)
	x = 'x{:02}'.format(i)
	y = 'y{:02}'.format(i)
	d_gate = (x, y, "AND")
	d_gate_value = gates[(x, y, "AND")]
	child_gates = list(filter(lambda x: x[0]==d_gate_value and x[2]=="OR", gates.keys()))
	e_gate = []
	if(len(child_gates) == 1):
		e_gate = child_gates[0]
	else:
		print("AMBIGUOUS E GATE")
	if(e_gate[0] == d_gate_value): return e_gate[1]
	else: return e_gate[0]

# set_val(wires, 1, 'x')
# set_val(wires, 2**2, 'x')
# set_val(wires, 2**4, 'y')
# print(get_val(wires, 'x'))
# print(get_val(wires, 'y'))
# print(solve_system(wires,gates))

# bad_bits = set()
# for i in range(46):
# 	set_val(wires, 2**i, 'x')
# 	set_val(wires, 0, 'y')
# 	if(solve_system(wires, gates) != 2**i):
# 		# print("D BAD BIT ", i)
# 		bad_bits.add(i)
# 	set_val(wires, 0, 'x')
# 	set_val(wires, 2**i, 'y')
# 	if(solve_system(wires, gates) != 2**i):
# 		# print("E BAD BIT ", i)
# 		bad_bits.add(i)
# 	set_val(wires, 2**i, 'x')
# 	set_val(wires, 2**i, 'y')
# 	if(solve_system(wires, gates) != 2**(i+1)):
# 		# print("F BAD BIT ", i)
# 		bad_bits.add(i)
# 		# print(get_ancestors(wires, 'z{:2}'.format(i)))
# 		# break

# a_gates = {}
# b_gates = {}
# c_gates = {}
# d_gates = {}
# e_gates = {}
# for i in range(46):
# 	x = 'x{:02}'.format(i)
# 	y = 'y{:02}'.format(i)
# 	z = 'z{:02}'.format(i)
# 	req_anc = xy_range(i)
# 	prev_anc = xy_range(i-1)
# 	for g in gates.keys():
# 		if (gates[g][0] == x and gates[g][2] == y) or (gates[g][0] == y and gates[g][2] == x):
# 			if gates[g][1] == "XOR": a_gates[i] = g
# 			elif gates[g][1] == "AND": d_gates[i] = g
# 		if gates[g][1] == "OR":
# 			gate_anc = get_ancestors(gates, g)
# 			if((gate_anc.issuperset(req_anc)) and 'x{:02}'.format(i+1) not in gate_anc and 'y{:02}'.format(i+1) not in gate_anc):
# 				e_gates[i] = g
# 		if gates[g][1] == "AND":
# 			gate_anc = get_ancestors(gates, g)
# 			if((gate_anc.issuperset(req_anc)) and 'x{:02}'.format(i+1) not in gate_anc and 'y{:02}'.format(i+1) not in gate_anc):
# 				c_gates[i] = g
# 			elif(gate_anc == set([x,y])):
# 				d_gates[i] = g
# 		if gates[g][1] == "XOR":
# 			gate_anc = get_ancestors(gates, g)
# 			if((gate_anc.issuperset(req_anc)) and 'x{:02}'.format(i+1) not in gate_anc and 'y{:02}'.format(i+1) not in gate_anc):
# 				b_gates[i] = g

swapped = []
swap = list(traverse_gates(gates))
swapped += (swap)
# print("SWAP {}".format(swap))
swap_tmp = gates[swap[0]]
gates[swap[0]] = gates[swap[1]]
gates[swap[1]] = swap_tmp
swap = list(traverse_gates(gates))
swapped += (swap)
# print("SWAP {}".format(swap))
swap_tmp = gates[swap[0]]
gates[swap[0]] = gates[swap[1]]
gates[swap[1]] = swap_tmp
swap = list(traverse_gates(gates))
swapped += (swap)
# print("SWAP {}".format(swap))
swap_tmp = gates[swap[0]]
gates[swap[0]] = gates[swap[1]]
gates[swap[1]] = swap_tmp
swap = list(traverse_gates(gates))
swapped += (swap)
# print("SWAP {}".format(swap))
swap_tmp = gates[swap[0]]
gates[swap[0]] = gates[swap[1]]
gates[swap[1]] = swap_tmp
# gates should be fixed?

swapped = list(swapped)
swapped.sort()

# This probably nowhere near a complete or universal solution
# But my brain is cooked from this one
# There is probably some binary trick you could use to exactly spot
# which gate is in the wrong spot...
print(",".join(swapped))
