# Implement a BST with insert and delete functions

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

	# delete a node by giving root
	def delete (self, value):
		if self is None:
			return

		else:
			node, parent = self.traverse(value, None)

			if node:
				numKids = node.numChildren()

				if numKids == 0:
					if parent:
						if parent.left is node:
							parent.left = None
						else:
							parent.right = None

						del Node
					else:
						self.data = None

				elif numKids == 1:

					if node.left:
						nodeChild = node.left
					else:
						nodeChild = node.right

					if parent:
						if parent.left is node:
							parent.left = nodeChild

						else:
							parent.right = nodeChild

					else:
						self.data = nodeChild.data
						self.left = nodeChild.left
						self.right = nodeChild.right

				elif numKids == 2:
					minimum, parentMin = node.right.mini(None)

					if parent:
						node.data = minimum.data

						if parentMin.left == minimum and minimum.right:
							parentMin.left = minimum.right

					else:
						self.data = minimum.data
						self.right = minimum.right

	def mini (self, parent):
		if self.left:
			self.left.min(self)
		else:
			return self, parent


	#@ look for parent
	def traverse (self, value, parent):
		if self.data > value:
			if self.left is None:
				return None, None

			return self.left.traverse(value, self)

		elif self.data < value:
			if self.right is None:
				return None, None

			return self.right.traverse(value, self)

		elif self.data == value:
			return self, parent

	def numChildren (self):
		count = 0

		if self.left:
			count +=1
		if self.right:
			count +=1

		return count


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(14)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(13)

# DFS in order
def inOrder(root):
	if root is None:
		return

	inOrder(root.left)
	print root.data
	inOrder(root.right)

# BFS
def levelOrder(root):
	if root is None:
		return

	curLevel = [root]

	while curLevel:
		nextLevel = []
		for node in curLevel:
			print node.data,
			if node.left:
				nextLevel.append(node.left)
			if node.right:
				nextLevel.append(node.right)
		print
		curLevel = nextLevel

#DFS pre order
def preOrder(root):
	if root is None:
		return

	print root.data
	preOrder(root.left)
	preOrder(root.right)

def postOrder(root):
	if root is None:
		return
	postOrder(root.left)
	postOrder(root.right)
	print root.data

print "levelOrder"
levelOrder(root)
print "preOrder"
preOrder(root)
print "inOrder"
inOrder(root)
print "postOrder"
postOrder(root)
print "delete 8"
root.delete(8)
print " "
preOrder(root)
print " "
inOrder(root)
print " "
levelOrder(root)
