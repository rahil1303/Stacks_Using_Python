class stack:
  def __init__(self,maxsize):
    self.maxsize = maxsize
    self.lists = []
    
   def __str__(self):
    values = self.list.reverse()
    values = [str(x) for x in self.lists]
    return "\n".join(values)
  
  def isFull(self):
    if len(self.lists) == self.maxsize:
      return True
    else:
      return False
  
  def isEmpty(self):
    if self.lists == []:
      return True
    else:
      return False
    
  def push(self,values):
    if self.isFull():
      return "The stack is Full"
    else:
      self.list.append(value)
      return "The value was entered successfully"
    
  
  
