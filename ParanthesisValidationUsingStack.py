# Valid Paranthesis
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
    
    def isempty(self):
        if self.top==None:
            return True
        return False



open=['(','[','{']
close=[')',']','}']

StackObject=Stack()
s=input("Enter Expression:")
for i in s:
    if i in open:
        StackObject.push(i)
    if i in close:
        if close.index(i)==open.index(StackObject.pop()):
            continue
        else:
            print("Invalid")
            break
if StackObject.isempty():
    print("Valid!!")
else:
    print("Invalid!")
