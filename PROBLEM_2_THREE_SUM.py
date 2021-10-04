class Multistack:
    def __init__(self,stacksize):
        self.numberstacks = 3
        self.custlist = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def isFull(self,stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
    
    def isEmpty(self,stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def indexoftop(self,stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self,item,stacknum):
        if self.isFull(stacknum):
            return "The stack is FULL"
        else:
            self.sizes[stacknum] += 1
            self.custlist[self.indexoftop(stacknum)] = item

    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return "The STACK is Empty"
        else:
            value = self.custlist[self.indexoftop(stacknum)]
            self.custlist[self.indexoftop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peak(self,stacknum):
        if self.isEmpty(stacknum):
            return "STACK is EMPTY"
        else:
            value = self.custlist[self.indexoftop[stacknum]]
            return value


customStack = Multistack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1,0)
customStack.push(2,0)
customStack.push(3,2)
print(customStack.pop(0))
