#singly linkedlist
#cannot move backward 
# LINKED LIST - NODES
# a linked list is a form of data structure which is connected in the form of node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(1)
node2 = Node(2)
node1.next=node2
node3 = Node(3)
node2.next = node3

# INSERTING 
# how to add new node in the beginning of the linked list 
# newnode =  Node(0)
# newnode.next = head
# hēad = newnode
# how to add a new node at the end
# current = head
# while current.next!=none:
#     current=current.next
# node1 = Node(6)
# current.next=node1
# Node.next=none

# types of linked list
# 1 singly linked list
# 2 doubly linked list
# 3 circular linked list  --tail.next=head

#need to delete the 3rd node also handle the edge case like if the 3rd node is not even there then what happens
head = node1
current = head
k = 3

# Handle edge case: if k=1, delete head
if k == 1:
    head = head.next
else:
    # Traverse to (k-1)th node
    # Need to move (k-2) steps to reach (k-1)th node
    count = 1
    while count < k-1:
        if current is None or current.next is None:
            print("Node not found")
            break
        current = current.next
        count += 1
    
    # Delete kth node if it exists
    if current and current.next:
        current.next = current.next.next
    else:
        print("3rd node doesn't exist")