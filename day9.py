DIR_DELTA = {
	"L": (0, -1),
	"R": (0, 1),
	"U": (-1, 0),
	"D": (1, 0)
}

DIAG_DELTA = [(1,1), (1,-1), (-1, 1), (-1,-1)]

f = open("day9.txt", "r")
input = f.readlines()

visited = set()
visited.add((0,0))

# Part 1: ROPE_LEN = 2
ROPE_LEN = 10
pos = [(0,0) for _ in range(ROPE_LEN)]

def closest_dir(curr, target, dirs):
	min_dir = None
	min_dir_distance = None
	for dir in dirs:
		distance = abs(target[0]-curr[0]-dir[0]) + abs(target[1]-curr[1]-dir[1])
		if (min_dir == None or min_dir_distance > distance):
			min_dir = dir 
			min_dir_distance = distance
	return min_dir

	
for line in input:
	parts = line.strip().split(" ")
	step = int(parts[1])
	
	for _ in range(step):
		pos[0] = (pos[0][0] + DIR_DELTA[parts[0]][0], pos[0][1] + DIR_DELTA[parts[0]][1])
		for i in range(1, ROPE_LEN):
			tail_dir = None	
			if (pos[i-1][0] == pos[i][0] or pos[i-1][1] == pos[i][1]):
				if (abs(pos[i-1][0] - pos[i][0]) > 1 or abs(pos[i-1][1] - pos[i][1]) > 1):
					tail_dir = closest_dir(pos[i], pos[i-1], DIR_DELTA.values())
			elif (abs(pos[i][0]-pos[i-1][0]) + abs(pos[i][1]-pos[i-1][1]) > 2):
				tail_dir = closest_dir(pos[i], pos[i-1], DIAG_DELTA)
	
			if (tail_dir):
				pos[i] = (pos[i][0] + tail_dir[0], pos[i][1] + tail_dir[1]) 
		
		visited.add(pos[ROPE_LEN-1])

print(len(visited)) 
