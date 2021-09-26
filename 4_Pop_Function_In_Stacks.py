Class Stack:
  def __init__(self):
    self.lists = []
  def __str__(self):
    values = self.lists.reverse()
    values = [str(x) for x in self.lists]
    return "\n".join(values)
    
  def isEmpty(self):
    if self.lists = []
      return True
    else:
      return False
      
  def push(self,value):
    self.lists.append(values)
    return "The elemet was successfully added in the list
    
  def pop(self):
    if self.lists.isEmpty():
      return "The Stack is Empty"
    else:
      self.lists.pop()
      
