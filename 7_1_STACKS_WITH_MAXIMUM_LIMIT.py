class stack:
  def __init__(self,maxsize):
    self.maxsize = maxsize
    self.list = []
  def __str__(self):
    values = self.list.reverse()
    values = [str(x) for x in self.list]
    return "\n".join(values)
  
