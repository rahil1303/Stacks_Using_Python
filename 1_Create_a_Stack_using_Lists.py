class Stack:
  def __init__(self):
    self.lists = []
  def __str__(self):
    values = self.lists.reverse()
    values = [str(x) for x in self.lists]
    return "\n".join(values)
    
