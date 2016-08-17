# implement a stack with push pop isEmpty peek and size methods
# last in first out

class Stack:
	def __init__ (self):
		self.values = []

	def push(self, value):
		self.values.append(value)

	def pop(self):
		return self.values.pop()

	def peek(self):
		return self.values[len(self.values)-1]

	def isEmpty(self):
		return len(self.values) == 0

	def size(self):
		return len(self.values)

someStack = Stack()

someStack.push(2)
someStack.push(16)

print someStack.pop()


# use a stack to reverse a string
# a little unnecessary but ok

def reversi (st):
	reverse = Stack()
	reverseStr = ""

	for item in st:
		reverse.push(item)

	for i in range(len(reverse.values)):
		reverseStr = reverseStr + reverse.pop()

	print reverseStr

reversi("wowe")

# implement a method that gets minimum of stack in O(1) time
# space is around O(n)

class minStack:
	def __init__ (self):
		self.miniStack = Stack()
		self.actualStack = Stack()
		self.curMin = 23048240234223422

	def push (self, value):
		if value <= self.curMin:
			self.miniStack.push(value)
			self.curMin = value

		self.actualStack.push(value)

	def pop (self):
		if self.actualStack.peek() == self.curMin:
			self.miniStack.pop()
			self.curMin = self.miniStack.peek()

		return self.actualStack.pop()

	def getMin (self):
		if self.curMin == 23048240234223422:
			print "does not exist"
		else:
			return self.curMin

theMini = minStack()

theMini.push(3)
theMini.push(4)
theMini.push(1)
theMini.push(16)
#shoudl print 1
print theMini.getMin()
theMini.pop()
theMini.pop()
#should print 3
print theMini.getMin()
