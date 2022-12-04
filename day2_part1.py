# my score if the combination is (my play, opponent play)
round_outcome = {
	("X", "A"): 3,
	("X", "B"): 0,
	("X", "C"): 6,
	
	("Y", "A"): 6,
	("Y", "B"): 3,
	("Y", "C"): 0,
	
	("Z", "A"): 0,
	("Z", "B"): 6,
	("Z", "C"): 3
}

shape_score = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

f = open("day2_input", "r")
input = f.readlines()

from functools import reduce

def calc(prev, curr):
	return prev + shape_score[curr[2]] + round_outcome[(curr[2], curr[0])]

print(reduce(calc, input, 0))
