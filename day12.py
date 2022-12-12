# !!! PART 2 !!! 

f = open("day12.txt", "r")
input = f.readlines()

grid = []
for idx, line in enumerate(input):
	grid.append(list(line.strip()))
	if (line.find("S")!= -1):
		start = (idx, line.index("S"))
	if (line.find("E") != -1):
		end = (idx, line.index("E"))
	
n = len(grid)
m = len(grid[0])

grid[start[0]][start[1]] = 'a'
grid[end[0]][end[1]] = 'z'

result = [[None for _ in range(m)] for _ in range(n)]
result[end[0]][end[1]] = 0
queue = [end]

def can_reach(curr, next):
	if (next[0] < 0 or next[0] >= n or next[1] < 0 or next[1] >= m):
		return False
	return ord(grid[next[0]][next[1]]) - ord(grid[curr[0]][curr[1]]) > -2

DIR = [(1,0), (0,1), (-1,0), (0,-1)]
while (len(queue) > 0):
	curr = queue.pop(0)
	for dir in DIR:
		next = (curr[0] + dir[0], curr[1] + dir[1])
		if (can_reach(curr, next) and (result[next[0]][next[1]] == None or result[curr[0]][curr[1]] + 1 < result[next[0]][next[1]])):
			result[next[0]][next[1]] = result[curr[0]][curr[1]] + 1
			queue.append(next)

mins = []
for i in range(n):
	for j in range(m):
		if (grid[i][j] == 'a' and result[i][j] != None):
			mins.append(result[i][j])

mins.sort()
print(mins[0])
