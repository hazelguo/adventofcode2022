f = open("day2_input", "r")
input = f.readlines()

from functools import reduce

def calc(prev, curr):
	round_score = (ord(curr[2]) - ord('X')) * 3
	shape_score = (ord(curr[0]) - ord('A') + ord(curr[2]) - ord('X')) % 3
	return prev + (shape_score if shape_score else 3) + round_score

print(reduce(calc, input, 0))
