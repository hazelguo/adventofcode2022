from functools import reduce

f = open("day4_input.txt", "r")
input = f.readlines()

def parse_tuple(str):
	return (int(str[:str.index('-')]), int(str[str.index('-')+1:]))

def calc(prev, curr):
	first = parse_tuple(curr[:curr.index(',')])
	second = parse_tuple(curr[curr.index(',')+1:])
	if (first[0] > second[0]):
		first, second = second, first
	
	return prev + ((first[0] <= second[0] <= first[1]) or (second[0] <= first[1] <= second[1]))

print(reduce(calc, input, 0))

