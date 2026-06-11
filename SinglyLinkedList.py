"""
Data Structure: Singly Linked List

Operations Implemented:
1. Insert at Beginning
2. Insert at End
3. Search Node
4. Delete First Node
5. Delete Last Node
6. Traverse List


Language: Python
"""

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
    
class SLL:
    def __init__(self,start=None):
        print("this called ")
        self.start = start
        
    def inserFirst(self,item):
        if self.start is None:
            # Means list is empty 
            self.start = Node(item=item,next=None)
        else:
            # Means list have some data 
            temp = self.start
            self.start = Node(item=item,next=temp)
    
    def inserLast(self,item):
        if self.start is not None:
            temp = self.start
            while(temp.next is not None):
                temp = temp.next
            temp.next = Node(item)
        else:
            self.start = Node(item)
    
            
    def searchitem(self,item):
        if self.start is not None:
            temp = self.start
            while temp.item is not None:
                if temp.item == item:
                    return temp
                temp = temp.next
            return None
                
    def deleteFirst(self):
        if self.start is not None:
            self.start = self.start.next
    def deleteLast(self):
        if self.start is not None:
            temp = self.start
            while(1):
                if temp.next.next is None:
                    temp.next = None
                    break
                temp = temp.next
                
    def __iter__(self):
        return iterator(self.start)
                
                
        
class iterator:
    def __init__(self,head):
        self.head = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.head:
            raise StopIteration
        data = self.head.item
        self.head = self.head.next
        return data

sll = SLL()
sll.inserFirst(5)
sll.inserFirst(2)
sll.inserFirst(7)
sll.inserLast(55)

for x in sll:
    print(x)
sll.deleteFirst()
print("after first delete")
for x in sll:
    print(x)
    
sll.deleteLast()
print("after last delete")
for x in sll:
    print(x)




        
        