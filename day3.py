from collections import Counter
from functools import reduce

f = open("day3_input", "r")
input = f.readlines()

result = 0

def get_list(str):
	return list(set([*str.strip()]))

for i in range(0, len(input), 3):
	sum = Counter(get_list(input[i]) + get_list(input[i+1]) + get_list(input[i+2]))
	for (char, num) in sum.most_common():
		if (num < 3):
			break
		result += ord(char) - ord('a') + 1 if ord(char) >= ord('a') else ord(char) - ord('A') + 27 

print(result)
