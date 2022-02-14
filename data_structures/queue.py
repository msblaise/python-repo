from collections import deque

class Queue:

	def __init__(self):
		# buf = self.buffer
		self.buffer = deque() # buffer is instance of deque (doubly ended queue)
		

	def enqueue(self, val):
		self.buffer.appendleft(val)

	def dequeue(self):
		return self.buffer.pop()

	def is_empty(self):
		return len(self.buffer)==0

	def size(self):
		return len(self.buffer)

	def display(self):
		for x in self.buffer:
			print(x)

pq = Queue()

pq.enqueue(5)
pq.enqueue(6)
pq.enqueue(9)

pq.display()

pq.dequeue()

print("\n")

pq.display()
