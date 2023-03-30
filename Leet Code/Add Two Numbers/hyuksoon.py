class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode()
        cur=answer
    
        carry=0
        while l1 or l2:
            num=carry
            carry=0
            if l1:
                num+=l1.val
                l1=l1.next
            if l2:
                num+=l2.val
                l2=l2.next
            if num>=10:
                carry=1
                num-=10
            cur.next=ListNode()
            cur=cur.next
            cur.val=num
        if carry==1:
            cur.next=ListNode()
            cur=cur.next
            cur.val=carry
 
        
        return answer.next
