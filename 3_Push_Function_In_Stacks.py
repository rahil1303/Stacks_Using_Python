class Stack:
  #### Create a Stack:
  def __init__(self):
    self.lists = []
  def __str__(self):
    values = self.lists.reverse()
    values = [str(x) for x in self.lists]
    return "\n".join(values)
  
  #### IsEmpty():
  def isEmpty(self):
    if self.lists = []:
      return True
    else:
      return False
    
 #### Push():
  def push(self,values):
    self.lists.append(values)
    return "The element is successfully added to the Stack"
    
