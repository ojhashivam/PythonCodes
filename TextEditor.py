#using 2 stack for text editor [undo, redo]
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


mainStack=Stack()
urStack=Stack()

str=input("Enter The String:")
operation=input("Enter The Operation:")

if operation[0]=='r':
    print("Enter Correct operation Sequence:")
else:
    for i in str:
        mainStack.push(i)
    for i in operation:
        if i=='u':
            urStack.push(mainStack.pop())
        elif i=='r':
            mainStack.push(urStack.pop())
    str="" #blanking str because of no future use
    while not mainStack.isempty():
        str=mainStack.pop()+str
    print(str)
