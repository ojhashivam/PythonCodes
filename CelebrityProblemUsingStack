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
        
    def size(self):
        if self.top==None:
            return 0
        curr=self.top
        s=0
        while curr:
            s+=1
            curr=curr.next
        return s
    
StackObject=Stack()

matrix=[

    [0,1,1,0],
    [1,0,1,0],
    [0,0,0,0],
    [1,0,1,0]
]

for i in range(len(matrix)):
    StackObject.push(i)

while StackObject.size()>=2:
    first=StackObject.pop()
    second=StackObject.pop()

    if matrix[first][second]==0:
        StackObject.push(first)
    else:
        StackObject.push(second)
element=StackObject.pop()

for i in range(len(matrix)):
    if i!=element:
        if matrix[element][i]==1 or matrix[i][element]==0:
            element=-1
            break
if element==-1:
    print("No-One IS The Celebrity!!")
else:
    print(element+1,"is the Cleberity")
