'''
HUFFMAN CODING
Compression algo that is used to compress data so as to not lose information
Greedy algo
'''
class node:
	def __init__(self, freq, symbol, left=None, right=None):
		self.freq = freq
		self.symbol = symbol
		self.left = left
		self.right = right
		self.huff = ''

def printNodes(node, val=''):
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node, then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

    # if node is edge node, then display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [ 5, 9, 12, 13, 16, 45]
nodes = []

# convert characters and frequencies into huffman tree nodes
for x in range(len(chars)):
	nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
	# sort all the nodes in ascending order based on their frequency
	nodes = sorted(nodes, key=lambda x: x.freq)

	# pick 2 smallest nodes
	left = nodes[0]
	right = nodes[1]

	# assign directional value to these nodes
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create new node as their parent
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	# remove the 2 nodes and add their parent as new node among others
	nodes.remove(left)
	nodes.remove(right)
	nodes.append(newNode)

printNodes(nodes[0])

