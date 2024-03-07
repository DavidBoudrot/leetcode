# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        curr2 = l2
        carryOver = 0
        while curr and curr2:
            curr2.val += curr.val + carryOver
            if curr2.val >= 10:
                carryOver = 1
                curr2.val = curr2.val - 10
            
            else:
                carryOver = 0
        
            if curr.next and not curr2.next:
                curr2.next = ListNode(0)
            
            elif curr2.next and not curr.next:
                curr.next = ListNode(0)

            elif not curr.next and not curr2.next and carryOver:
                curr.next = ListNode(0)
                curr2.next = ListNode(0)
            
            curr = curr.next
            curr2 = curr2.next

        return l2
