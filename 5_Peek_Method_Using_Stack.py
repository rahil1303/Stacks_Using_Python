class Stack:
  def __init__(self):
    self.lists = []
  def __str__(self):
    values = self.lists.reverse()
    values = [str(x) for x in self.lists)
    return "\n".join(values)
              
  def isEmpty(self):
    if self.lists = []:
       return True
    else:
       return False
              
  def push(self,values):
              self.lists.append(values)
              return "The element has been successfully been added"
          
   def pop(self):
              if self.isEmpty():
                return "The stack is empty"
              else:
                self.lists.pop()
              
   def peek(self):
              if self.isEmpty():
                return "Stack is Empty"
              else:
                self.lists[len(self.lists)-1]
              
            
  
