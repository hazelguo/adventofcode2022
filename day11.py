# SAMPLE
# MONKEY_COUNT = 4
# MOD = 96577
# 
# ITEMS = [
# 	[79, 98],
# 	[54, 65, 75, 74],
# 	[79, 60, 97],
# 	[74]
# ]
# 
# OPERATIONS = [
# 	lambda x: x * 19,
# 	lambda x: x+6,
# 	lambda x: x*x,
# 	lambda x: x+3
# ]
# 
# TESTS = [ 23,19,13,17 ]
# 
# TEST_ACTION = [ (3, 2), (0,2), (3, 1), (1,0) ] # (False, True)

MONKEY_COUNT = 8
MOD = 9699690
ITEMS = [
	[52, 60, 85, 69, 75, 75],
	[96, 82, 61, 99, 82, 84, 85],
	[95, 79],
	[88, 50, 82, 65, 77],
	[66, 90, 59, 90, 87, 63, 53, 88],
	[92, 75, 62],
	[94, 86, 76, 67],
	[57]
]
OPERATIONS = [
	lambda x: x*17,
	lambda x:x+8,
	lambda x:x+6,
	lambda x:x*19,
	lambda x:x+7,
	lambda x:x*x,
	lambda x:x+1,
	lambda x:x+2
]
TESTS = [13,7,19,2,5,3,11,17]
TEST_ACTION = [(7,6), (7,0), (3,5), (1,4), (0,1), (4,3), (2,5), (2,6)]

result = [0 for _ in range(MONKEY_COUNT)]

for i in range(10000 * MONKEY_COUNT):
	idx = i % MONKEY_COUNT
	while (len(ITEMS[idx]) > 0):
		item = ITEMS[idx].pop(0)
		result[idx] += 1
		# PART 1
		# level = int(OPERATIONS[idx](item)/3) 
		level = OPERATIONS[idx](item) % MOD
		target = TEST_ACTION[idx][level % TESTS[idx] == 0]
		ITEMS[target].append(level)
	
result.sort()
print(result)	
		
		 	
