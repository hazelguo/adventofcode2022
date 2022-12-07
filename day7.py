class TreeNode:
	def __init__(self, name, sizeStr, parent):
		self.name = name
		self.size = int(sizeStr) if sizeStr else None 
		self.children = [] # references to other nodes
		self.parent = parent

PART1_SIZE_LIMIT = 100000

def parse_input(input):
	root = TreeNode("/", None, None)
	curr = root
	idx = 1
	input_length = len(input)
	while (idx < input_length):
		line = input[idx]
		idx += 1
		if (line.startswith("$ ls")):
			while (idx < input_length and (not input[idx].startswith("$"))):
				parts = [i.strip() for i in input[idx].split(" ")]
				idx += 1
				child_node = TreeNode(parts[1], None if parts[0] == "dir" else parts[0], curr)
				curr.children.append(child_node)
		else:
			parts = [i.strip() for i in line.split(' ')] 
			if (parts[2] == ".."):
				curr = curr.parent
			else:
				for child in curr.children:
					if (child.name == parts[2]):
						curr = child
						break 
	return root

def print_tree(curr):
	children = []
	for i in curr.children:
		children.append(i.name)
	print("name: ", curr.name, "size: ", curr.size, "children: ", len(children), " ".join(children))
	for i in curr.children:
		print_tree(i)	

############ Part 1 #################
result = 0

def compute_size(curr):
	global result

	children_size = 0		
	for child in curr.children:
		children_size += compute_size(child)
	if (curr.size == None):
		if (children_size < PART1_SIZE_LIMIT):
			result += children_size
	return children_size + (curr.size if curr.size else 0)	

############ end #################

def compute_root_size(curr):
	children_size = 0		
	for child in curr.children:
		children_size += compute_root_size(child)
	return children_size + (curr.size if curr.size else 0)


def min_w_None(x, y):
	if (x == None or y == None):
		return x if x else y
	else:
		return min(x,y)

# find the smallest tree node with size larger than target
def find_smallest_greater(curr, target):
	children_result = None
	children_size = 0

	for child in curr.children:
		child_size, child_result = find_smallest_greater(child, target)
		children_result = min_w_None(children_result, child_result)
		children_size += child_size

	curr_size = children_size + (curr.size if curr.size else 0)
	return (curr_size, min_w_None(children_result, curr_size if (curr_size >= target and curr.size == None) else None))

f = open("day7.txt", "r")
input = f.readlines()

root = parse_input(input)
root_size = compute_root_size(root)
print(find_smallest_greater(root, root_size-40000000))
