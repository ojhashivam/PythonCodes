class NewNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.top=None
    
    def push(self,data):
        new=NewNode(data)
        new.next=self.top
        self.top=new

    def pop(self):
        if self.top==None:
            return False
        else:
            c=self.top.data
            self.top=self.top.next
            return c
            

    def printStack(self):
        c=self.top
        while c:
            print(c.data,end='')
            c=c.next
    
    def isempty(self):
        if self.top==None:
            return True
        return False

    def StringReversal(self,s):
        for i in s:
            self.push(i)
        s=""
        while not self.isempty():
            s+=self.pop()
        return s



#StackObject=Stack()
#StackObject.push(3)
#StackObject.push(4)
#StackObject.pop()
#StackObject.isempty()
#StackObject.printStack()
#print(StackObject.StringReversal("Hello Everyone"))
