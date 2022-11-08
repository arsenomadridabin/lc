# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_1 = []
        while l1.next:
            l_1.append(str(l1.val))
            l1 = l1.next
        l_1.append(str(l1.val))
        l_2 = []
        while l2.next:
            l_2.append(str(l2.val))
            l2 = l2.next
        l_2.append(str(l2.val))
        l_1 = int("".join(l_1)[::-1])
        l_2 = int("".join(l_2)[::-1])
        l_3 = l_1 + l_2
        l_3 = str(l_3)
        node = ListNode(val=l_3[0],next=None)
        for val in l_3[1:]:
            node = ListNode(val=val,next=node)
        return node
            
        
        