class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

class stack:
    def __init__(self):
        self.LinkedList = LinkedList()
        
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head = None
