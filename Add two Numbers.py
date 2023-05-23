from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        carry = 0

        # while l1 or l2 or carry:
        #     val1 = (l1.val if l1 else 0)
        #     val2 = (l2.val if l2 else 0)
        #     carry, out  = divmod(val1+val2 + carry, 10)
            
        # result_tail.next = ListNode(out)
        # result_tail = result_tail.next

        #     l1 = (l1.next if l1 else None)
        #     l2 = (l2.next if l2 else None)

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None        
    
        return result.next

mysolution = Solution()
mysolution.addTwoNumbers(l1 = ListNode(1, ListNode(2, ListNode(4))), l2 = ListNode(4, ListNode(5, ListNode(7))))

