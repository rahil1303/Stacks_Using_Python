class Node:
  def __init__(self,value = node):
    self.value = value
    self.next = next
class LinkedList:
  def __init__(self):
    self.head = None

class stack:
  def __init__(self):
    self.LinkedList = LinkedList()
    
  def isEmpty(self):
    if self.LinkedList == None:
      return True
    else:
      return False
   
  def push(self,value):
    node = node(value)
    node.next = self.LinkedList.head
    self.LinkedList.head = node
    
  def pop(self):
    if self.isEmpty():
      return "there is no element in the stack"
    else:
      nodeValue = self.LinkedList.head.value
      self.LinkedList.head = self.LinkedList.head.next
      return nodeValue
  
  
  
  
  
  
  
  
  
  
