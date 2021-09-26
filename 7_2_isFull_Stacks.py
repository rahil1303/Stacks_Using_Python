class stack:
  def __init__(self,maxsize):
    self.maxsize = maxsize
    self.list = []
  def __str__(self):
    values = self.lists.reverse()
    values = [str(x) for x in self.lists]
    return "\n".join(values)
  
  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False
    
  def isFul(self):
    if len(self.lists) == self.maxsize:
      return True
    else:
      return False
