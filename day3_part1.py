from collections import Counter
from functools import reduce

f = open("day3_input", "r")
input = f.readlines()

def calc(prev, curr):
	half_len = int(len(curr)/2)
	sum = Counter(list(set([*curr[:half_len]])) + list(set([*curr[half_len:]])))

	result = 0
	for (char, num) in sum.most_common():
		if (num < 1):
			break
		result += ord(char) - ord('a') + 1 if ord(char) >= ord('a') else ord(char) - ord('A') + 27 
	return prev + result


print(reduce(calc, input, 0))
