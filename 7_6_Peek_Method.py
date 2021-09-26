class stack:
  def __init__(self,maxsize):
    self.maxsize = maxsize
    self.lists = []
  
  def __str__(self):
    values = self.lists.reverse()
    values = [str(x) for x in self.lists]
    return "\n".join(values)
  
  def isEmpty(self):
    if self.lists = []:
      return True
    else:
      return False
    
  def isFull(self):
    if len(self.lists) == self.maxsize:
      return True
    else:
      return False
    
  def push(self,maxsize):
    if self.isFull():
      return "The stack is Full"
    else:
      self.list.append(value)
      return "The value is successfully inserted"
    
   
  def pop(self):
    if self.isEmpty():
      return "The stack is empty"
    else:
      self.lists.pop()
      return "Value popped out"
    
  def peek(self):
    if self.isEmpty():
      return "There is no element is the stack"
    else:
      self.lists[len(self.lists)-1]
