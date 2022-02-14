'''
floyd cycle finding algo implementation (tortoise and the hare algo):
- traverse linked list using two pointers.
- move one pointer(slow_pointer) by one and another pointer(fast_pointer) by two.
- if these pointers meet at the same node then there is a loop. 
if pointers do not meet then linked list doesn’t have a loop.
'''

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next 

	def detectLoop(self):
		slow_pointer = self.head
		fast_pointer = self.head
		while(slow_pointer and fast_pointer and fast_pointer.next):
			slow_pointer = slow_pointer.next
			fast_pointer = fast_pointer.next.next
			if slow_pointer == fast_pointer:
				return True
			
# driver code
llist = LinkedList()
llist.push(20)
llist.push(70)

# create a loop
llist.head.next = llist.head
if(llist.detectLoop()):
	print("Found Loop")
else:
	print("No Loop")





