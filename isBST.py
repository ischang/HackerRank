# taken from my bstInsertDelete.py code! :D
class Node:
	def __init__ (self, value):
		self.right = None
		self.left = None
		self.data = value

	def insert(self, value):
		if self.data is None:
			self.data = value

		else:
			if self.data > value:
				if self.left is None:
					self.left = Node(value)
				else:
					self.left.insert(value)
			else:
				if self.right is None:
					self.right = Node(value)
				else:
					self.right.insert(value)

# appends an in order traversal of a BST
def inOrder(root, arr):
	if root is None:
		return

	inOrder(root.left, arr)
	arr.append(root.data)
	inOrder(root.right, arr)

# checks if the array is sorted
def isBST (root):
	arr = []
	inOrder(root, arr)

	# if the array is sorted in ascending order, it's a BST
	# faster than lambdas, hence using this
	if all(arr[i] < arr[i+1] for i in xrange(len(arr)-1)):
		return True

	return False

# this creates a false BST
falsie = Node(8)
falsie.left = Node(32)
falsie.right = Node(12)
falsie.left.left = Node(14)
falsie.left.right = Node(35)

# this creates a valid BST
root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(14)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(13)

print isBST(root)
print isBST(falsie)