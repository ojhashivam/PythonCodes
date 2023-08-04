class create_Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtFirst(self,data):
        new=create_Node(data)
        new.next=self.head
        self.head=new
    def printLL(self):
        if self.head==None:
            print("EMPTY LINKED LIST!!")
        else:
            n=self.head
            while n!=None:
                print('-->',n.data,end='')
                n=n.next
    def insertAtIndex(self,data,index):
        if index==0:
            self.insertAtFirst(data)
        else:
            new=create_Node(data)
            loop=0
            tempHead=self.head
            while(loop!=index-1):
               tempHead=tempHead.next
               loop+=1
            new.next=tempHead.next
            tempHead.next=new
    def deleteFirst(self):
        if self.head==None:
            print("Underflow")
        else:
            self.head=self.head.next
    
    def deleteAtIndex(self,index):
        if index==0:
            self.deleteFirst()
        else:
            temp=self.head
            loop=0
            while loop!=index-1:
                temp=temp.next
                loop+=1
            temp.next=temp.next.next  
    def InsertAtChoice(self):
        data=int(input("Enter Data:"))
        index=int(input("Enter Index:"))
        if index==0:
            self.insertAtFirst(data)
        else:
            self.insertAtIndex(data,index)
    
    def deleteAtChoice(self):
        index=int(input("Enter Index:"))
        if index==0:
            self.deleteFirst()
        else:
            self.deleteAtIndex(index)
    
    def ReplaceMax(self,value):
        if self.head==None:
            print("Empty LL")
            return
        maximum=self.head
        curr=self.head
        while curr.next!=None:
            if curr.data>=maximum.data:
                maximum=curr
                curr=curr.next
            curr=curr.next
        maximum.data=value

    def SumOdd(self):
        s=0
        pos=0
        curr=self.head
        while curr.next!=None:
            if pos%2==0:
                pos+=1
                curr=curr.next
                continue
            else:
                s+=curr.data
                pos+=1
                curr=curr.next
        return s

    def InplaceReversal(self):

        prev=None
        curr=self.head

        while curr!=None:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        self.head=prev


        



            







l=LinkedList()
l.insertAtFirst(10)
l.insertAtFirst(20)
l.insertAtFirst(30)
l.insertAtFirst(40)
l.insertAtFirst(50)
l.insertAtFirst(60)
l.insertAtFirst(70)
#l.deleteFirst()
#l.insertAtIndex(2,6)
#l.deleteAtIndex(0)
#l.InsertAtChoice()
#l.deleteAtChoice()
#l.ReplaceMax(800)
l.printLL()
#p=l.SumOdd()
#print('\nSum Of The Values At Odd Position Is:', p,'\n')
#l.InplaceReversal()
#print('\n')
#l.printLL()