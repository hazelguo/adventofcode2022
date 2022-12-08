f = open("day8.txt", "r")
input = f.readlines()

grid = []
for line in input:
	grid.append([int(i) for i in list(line.strip())])

n = len(grid)
m = len(grid[0])
result = []
for i in range(n):
	result.append([1 for j in range(m)])

# Look down and look right
# col[i][j]: the closest index of tree taller or same height than j (in the same col, before i)
col = [[0 for k in range(0, 10, 1)] for j in range(m)]
row = [[0 for k in range(0, 10, 1)] for i in range(n)]
for i in range(n):
	for j in range(m):
		result[i][j] *= j - row[i][grid[i][j]]
		result[i][j] *= i - col[j][grid[i][j]]
		for k in range(grid[i][j], -1, -1):
			col[j][k] = i
			row[i][k] = j


max_score = 0

# Look up and look left
col = [[n-1 for k in range(0, 10, 1)] for j in range(m)]
row = [[m-1 for k in range(0, 10, 1)] for i in range(n)]
for i in range(n-1, -1, -1):
	for j in range(m-1, -1, -1):
		result[i][j] *= row[i][grid[i][j]] - j
		result[i][j] *= col[j][grid[i][j]] - i 
		max_score = max(result[i][j], max_score)		
		for k in range(grid[i][j], -1, -1):
			col[j][k] = i
			row[i][k] = j

print(max_score)
