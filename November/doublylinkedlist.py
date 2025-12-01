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

