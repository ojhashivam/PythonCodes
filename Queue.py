class NewNode:

    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def Enqueue(self,data):
        c=NewNode(data)
        if self.front==None:
            self.front=c
            self.rear=c
        else:
            self.rear.next=c
            self.rear=c

    def Dequeue(self):
        if self.front==None:
            print("Empty")
            return
        else:
            self.front=self.front.next

    
    def PrintQueue(self):
        if self.front==None:
            print("Empty")
            return
        else:
            print('\n')
            c=self.front
            while c:
                print(c.data,end=' ')
                c=c.next



#QueueObject=Queue()
#QueueObject.Enqueue(1)
#QueueObject.Enqueue(2)
#QueueObject.Enqueue(3)
#QueueObject.Enqueue(4)
#QueueObject.PrintQueue()
#QueueObject.Dequeue()
#QueueObject.PrintQueue()
