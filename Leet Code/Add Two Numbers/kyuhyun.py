# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode(0)
        answer = res
        sum = 0
        while l1 or l2 or sum:
        
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2: 
                sum += l2.val
                l2 = l2.next

            answer.next = ListNode(sum % 10)
            answer = answer.next
            sum //= 10

        return res.next
