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