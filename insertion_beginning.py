class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
def display(head):
    temp=head
    while temp is not None:
        print(temp.data,end="->")
        temp=temp.next
    print("None")
print("Original linked list")
display(head)
print("/nInsertion at begining")
New_node=Node(5)
New_node.next=head
head=New_node
display(head)
    
