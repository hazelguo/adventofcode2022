from functools import reduce

def parse_input(input):
	init_state = []
	for move_start_idx, line in enumerate(input):
		if (line[0] == '\n'):
			break
		init_state.append(line)
	
	# parse moves
	moves = []
	for i in range(move_start_idx+1, len(input)):
		line = input[i].split(" ")
		moves.append((int(line[1]), int(line[3]), int(line[5])))

	# parse the initial state
	queues = [[] for _ in range(int(len(init_state[0])/3))] 
	for idx, char in enumerate(init_state[-1]):
		try:
			col = int(char)
			for i in range(len(init_state)-2, -1, -1):
				if (init_state[i][idx] != ' '):
					queues[col].append(init_state[i][idx])
		except:
			pass	
	

	return queues, moves 


f = open("day5_input.txt", "r")
input = f.readlines()

queues, moves = parse_input(input)

for count, from_col, to_col in moves:
	# part 1
	# for _ in range(count):
	# 	queues[to_col].append(queues[from_col].pop())

	# part 2
	len_from_col = len(queues[from_col])
	for i in range(count):
		queues[to_col].append(queues[from_col].pop(len_from_col-count))

print(reduce(lambda prev, curr: prev + (queues[curr][-1] if len(queues[curr]) > 0 else " "), range(1, len(queues)), " ")) 
