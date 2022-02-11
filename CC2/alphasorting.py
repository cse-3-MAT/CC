
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None

def printlist(head):
	if (not head):
		print("Empty List")
		return

	while (head != None):
		print(head.data, end = " ")
		if (head.next):
			print(end = "-> ")
		head = head.next
	print()


def isVowel(x):
	return (x == 'a' or x == 'e' or x == 'i'
			or x == 'o' or x == 'u' or x == 'A'
			or x == 'E' or x == 'I' or x == 'O'
			or x == 'U')

def arrange(head):
	newHead = head

	latestVowel = None

	curr = head

	
	if (head == None):
		return None
.
	if (isVowel(head.data)):

		latestVowel = head

	else:

		while (curr.next != None and
			not isVowel(curr.next.data)):
			curr = curr.next


		
		if (curr.next == None):
			return head

		
		latestVowel = newHead = curr.next
		curr.next = curr.next.next
		latestVowel.next = head

	
	while (curr != None and curr.next != None):
		if (isVowel(curr.next.data)):
			
			if (curr == latestVowel):
				
				latestVowel = curr = curr.next
			else:

			
				temp = latestVowel.next

				
				latestVowel.next = curr.next

			
				latestVowel = latestVowel.next

				curr.next = curr.next.next

				latestVowel.next = temp

		else:

			curr = curr.next

	return newHead


if __name__ == '__main__':
	
	# Initialise the Linked List
	head = Node('a')
	head.next = Node('b')
	head.next.next = Node('c')
	head.next.next.next = Node('e')
	head.next.next.next.next = Node('d')
	head.next.next.next.next.next = Node('o')
	head.next.next.next.next.next.next = Node('x')
	head.next.next.next.next.next.next.next = Node('i')

	
	print("Linked list before :")
	printlist(head)

	head = arrange(head)

	
	print("Linked list after :")
	printlist(head)


