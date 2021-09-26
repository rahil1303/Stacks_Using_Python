Class Stack:
  def __init__(self):
    self.list = []
  def __str__(self):
    values = self.lists.reverse()
    values = [str(x) for x in self.lists]
    return "\n".join(values)
  
  def isEmpty(self):
    if self.lists == []:
      return True
    else:
      return False
    
  def push(self,values):
    self.lists.append(values)
    return "The element is added successfully"
  
  def pop(self):
    def pop(self):
      if self.isEmpty():
        return "The stack is Empty"
      else:
        return self.lists.pop()
      
  def peek(self):
    if self.isEmpty():
      return "The stack is Empty"
    else:
      return self.list[len(self.lists)-1]
    
   
 def delete(self):
  self.list = None
