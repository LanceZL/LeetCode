from typing import Optional

from utils.list_node import ListNode


class MergeTwoLists:
    """
    Problem:    021. Merge Two Lists
    Link:       https://leetcode.com/problems/merge-two-sorted-lists/
    Solution:
    """

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Sorted List"""
        # Base Case
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # result list, result points to a dummy node. result.next is the actual head.
        result = ListNode()
        current = result
        # Use two pointer to merge two sorted list
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next  # Move current pointer of result list to next

        # One of l1 and l2 might not be None
        if l1 is not None:
            current.next = l1
        if l2 is not None:
            current.next = l2

        # Return result list
        return result.next
