# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr1 = head
        curr2 = head

        while (curr1 != None and curr2 != None):
            curr1 = curr1.next
            curr2 = curr2.next

            if curr2 != None:
                curr2 = curr2.next

            if curr1 != None and curr2 != None:
                if curr1 == curr2:
                    return True

        return False
