class Node:
	
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class LinkedList:

	def __init__(self):
		self.head = None


	def print_list(self):

		node = self.head

		while node != None:
			print(node.data)
			node = node.next



	def insert_at_head(self, data):

		self.head = Node(data, self.head)

		return True



	def insert_at_tail(self, data):

		# if empty list, insert as head node
		if self.head==None:
			self.head = Node(data, None)

		else:
			current_node = self.head
			while current_node.next != None:
				current_node = current_node.next
			current_node.next = Node(data, None)

		return True


	def insert_at_index(self, data, index):

		# if empty list, insert as head node
		if self.head==None:
			self.head = Node(data, None)
			return True

		i=0
		current_node = self.head

		while i<index:

			# if index out of range, do not insert
			if current_node.next==None:
				return False

			current_node = current_node.next
			i+=1

		current_node.next = Node(current_node.data, current_node.next)
		current_node.data = data

		return True


	def delete_at_index(self, index):

		# if index negative, do not delete
		if index<0:
			return False

		i=0
		prev_node = None
		current_node = self.head

		while i<index:

			# if index out of range, do not delete 
			if current_node.next==None:
				return False

			prev_node = current_node
			current_node = current_node.next
			i+=1

		if prev_node==None:
			self.head = current_node.next
		else:
			prev_node.next = current_node.next

		return True


	def reverse(self, node):

		if node==None or node.next == None:
			self.head = node
			return

		self.reverse(node.next)
		node.next.next = node
		node.next = None



if __name__ == '__main__':

	##### TESTS #####

	print("Empty list:")
	list1 = LinkedList()
	list1.print_list()

	print("Node inserted at head:")
	list1.insert_at_head('hello')
	list1.print_list()

	print("Node inserted at head:")
	list1.insert_at_head(5)
	list1.print_list()

	print("Node inserted at tail:")
	list1.insert_at_tail('end')
	list1.print_list()

	print("Node inserted at index 2:")
	list1.insert_at_index(11,2)
	list1.print_list()

	print("Node inserted at index 0:")
	list1.insert_at_index('start',0)
	list1.print_list()

	print("Node inserted out of range:")
	list1.insert_at_index('Should not see this',100)
	list1.print_list()

	print("Node deleted at index 1:")
	list1.delete_at_index(1)
	list1.print_list()

	print("Reversed list:")
	list1.reverse(list1.head)
	list1.print_list()





