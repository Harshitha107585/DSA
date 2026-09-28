class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
         
class MyLinkedList:

    def __init__(self):
        self.head = None
            
    def get(self, index: int) -> int:
        temp = self.head
        count = 0
        while temp != None:
            if count == index:
                return temp.val
            count+=1
            temp = temp.next
        return -1        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return 
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node     

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head  
        count = 0  
        while temp != None and count < index-1:
            temp = temp.next
            count+=1
        if temp == None:
            return
        new_node = Node(val)
        new_node.next = temp.next
        temp.next = new_node    

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return 
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp.next !=None and count < index -1:
            temp = temp.next
            count+=1
        if temp.next == None:
            return
        temp.next = temp.next.next    


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)