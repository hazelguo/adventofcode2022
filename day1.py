from functools import reduce
import heapq

f = open("day1_input", "r")
input = f.readlines()

# prev = (prev_max, prev_sum)
def calc(prev, curr):
	prev_max, prev_sum = prev
	try:
		val = int(curr)
	except:
		heapq.heappush(prev_max,prev_sum)
		if (len(prev_max) > 3):
			heapq.heappop(prev_max)
		return (prev_max, 0)
	else:
		return (prev_max, prev_sum + val) 

print(sum(reduce(calc, input, ([],0))[0]))

