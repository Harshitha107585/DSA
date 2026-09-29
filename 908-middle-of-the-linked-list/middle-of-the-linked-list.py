# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        temp = head
        n = 0
        while temp!=None:
            n+=1
            temp = temp.next
        temp = head
        i = 0
        while i < n//2:
            temp = temp.next
            i+=1
        return temp     


        