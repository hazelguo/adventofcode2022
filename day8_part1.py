f = open("day8.txt", "r")
input = f.readlines()

grid = []
for line in input:
	grid.append([int(i) for i in list(line.strip())])


n = len(grid)
m = len(grid[0])
visible = []
for i in range(n):
	visible.append([False for j in range(m)])

def calc(i, j, row_i, col_j):
	if (col_j == None) or (col_j < grid[i][j]):
		visible[i][j] = True
	new_col = max(col_j if col_j else 0, grid[i][j])
		
	if (row_i == None) or (row_i < grid[i][j]):
		visible[i][j] = True
	new_row = max(row_i if row_i else 0, grid[i][j])
	
	return new_row, new_col

# Look down and look right
col = [None for j in range(m)]
row = [None for i in range(n)]
for i in range(n):
	for j in range(m):
		row[i], col[j] = calc(i, j, row[i], col[j])

# Look up and look left
col = [None for j in range(m)]
row = [None for i in range(n)]
for i in range(n-1, -1, -1):
	for j in range(m-1, -1, -1):
		row[i], col[j] = calc(i, j, row[i], col[j])

result = 0
for i in range(n):
	for j in range(m):
		result += 1 if visible[i][j] else 0

print(result)	
