# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # res = ListNode((l1.val+l2.val)%10, ListNode((l1.val+l2.val)//10))
        if l1.next == None and l2.next == None:
            res = ListNode((l1.val + l2.val) % 10)
            answer = res
            if l1.val + l2.val >= 10:
                res.next = ListNode((l1.val + l2.val) // 10)
        else:
            res = ListNode((l1.val + l2.val) % 10, ListNode((l1.val + l2.val) // 10))
            answer = res
            while l1.next != None or l2.next != None:
                if l1.next == None:
                    l1.next = ListNode()
                if l2.next == None:
                    l2.next = ListNode()
                l1 = l1.next
                l2 = l2.next
                if res.next == None:
                    res.next = ListNode()
                res = res.next
                if res.val + l1.val + l2.val >= 10:
                    res.next = ListNode((res.val + l1.val + l2.val) // 10)
                res.val = (res.val + l1.val + l2.val) % 10

        return answer
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
