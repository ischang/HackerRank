# implement a queue with enqueue and dequeue options
# first in first out

class Queue:
	def __init__ (self):
		self.values = []

	# dun wanna spell enqueue
	def en(self, value):
		self.values.append(value)

	# dun wanna spell dequeue
	def de(self):
		return self.values.pop(len(self.values)-1)

Q = Queue()
Q.en(2)
Q.en(4)
print Q.values
print Q.de()
print Q.values