
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to help with merging
        dummy = ListNode(-1)
        current = dummy

        # Merge lists while both are not empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append the remaining nodes of the non-empty list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list starting from the next node of the dummy
        return dummy.next
