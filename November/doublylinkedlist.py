'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def adddoubly(head, data):
    if head is None:
        return Node(data)
    new = Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new
    new.prev = temp
    return head


# Test case: [2,4,6]
head = Node(2)
adddoubly(head, 4)
adddoubly(head, 6)
'''
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def adddoubly(head, data):
    if head is None:
        return Node(data)
    new = Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new
    new.prev = temp
    return head

def addatk(head, data, k):
    if head is None:
        return Node(data)
    new = Node(data)
    temp = head
    count = 1
    while count < k-1 and temp.next:
        temp = temp.next
        count += 1
    new.next = temp.next
    if temp.next:
        temp.next.prev = new
    temp.next = new
    new.prev = temp


k = 2
head = Node(1)
adddoubly(head, 2)
adddoubly(head, 3)
adddoubly(head, 4)
addatk(head, 5, k)
# Print the list
temp = head
while temp:
    print(temp.data)
    temp = temp.next

'''


'''
class Solution:
    def insertAtPos(self, head, p, x):
        new = Node(x)
        temp = head
        for i in range(p):
            temp = temp.next
        new.next = temp.next
        if temp.next:
            temp.next.prev = new
        temp.next = new
        new.prev = temp
        return head
    
'''


'''
# 206. Reverse Linked List - LeetCode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev
    
    # Recursive approach
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        
        return new_head
'''



#circular linked list
#1. insertion of a node in circular linked list

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_circular(head, data):
    n1 = CircularNode(data)
    
    # Edge case1: no nodes
    if head is None:
        n1.next = n1
        return n1
    
    # Edge case2: one node
    if head.next == head:
        n1.next = head
        head.next = n1
        return n1
    
    # Find last node
    temp = head
    while temp.next != head:
        temp = temp.next
    
    # Insert before head
    temp.next = n1
    n1.next = head
    return n1

head = None
head = insert_circular(head, 1)  
head = insert_circular(head, 2)  
head = insert_circular(head, 3)  


temp = head
print(temp.data, end=" ")
temp = temp.next
while temp != head:
    print(temp.data, end=" ")
    temp = temp.next
