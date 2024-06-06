from typing import List


class ListNode:
    """Node in single list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    """
        Helper class that can :
            1. Build a list by a list of integers.
            2. Compare two list, check if they are equal.
    """
    @staticmethod
    def build_list(nums: List[int]) -> ListNode:
        """
            Build a LinkedList by a list of integers.
            Returns the head of this list.
        """
        if nums is None:
            return None
        
        n = len(nums)
        # Empty list.
        if n == 0:
            return None
        
        # Headnode
        head = ListNode(nums[0])
        cur = head

        # Build linked list.
        for i in range(1, n):
            cur.next = ListNode(nums[i])
            cur = cur.next
        
        return head


    @staticmethod
    def compare(l1: ListNode, l2: ListNode) -> bool:
        """
            Returns True if value of each nodes in one list equals to another one, in the same position.
        """
        return LinkedList.value_of(l1) == LinkedList.value_of(l2)

    @staticmethod
    def value_of(l: ListNode) -> List[int]:
        """
            Returns a list that contains each node's value of the given list.
        """
        if l is None:
            return None

        values = []
        # Iterate the list, add node's value into the values.
        cur = l
        while cur is not None:
            values.append(cur.val)
            cur = cur.next

        return values

    @staticmethod
    def print_list(l: ListNode) -> str:
        """
            Returns a formated string represented a list.
        """
        if l is None:
            return ""
        
        values = LinkedList.value_of(l)
        return " -> ".join(str(x) for x in values)

