from collections import Counter

MARKER_LEN = 14

f = open("day6.txt", "r")
input = f.readlines()[0]

chars = Counter()
for idx, char in enumerate(input):
	chars[char] += 1
	if (idx >= MARKER_LEN):
		char_to_delete = input[idx-MARKER_LEN]
		chars[char_to_delete] -= 1
		if (chars[char_to_delete] == 0):
			del chars[char_to_delete]
	if (len(chars.keys()) == MARKER_LEN):
		print(idx+1)
		break
