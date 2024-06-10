from typing import List


class ListNode:
    """Node in single list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        values = self.__to_array()
        if len(values) == 0:
            return "None"

        return " -> ".join(str(x) for x in values)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        if other is None:
            return False

        p1, p2 = self, other
        while p1 is not None and p2 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return p1 is None and p2 is None

    def __to_array(self) -> List[int]:
        """Guranteed that self is not none when call this method"""
        values = []
        cur = self
        while cur is not None:
            values.append(cur.val)
            cur = cur.next
        return values

    def __len__(self):
        return len(self.__to_array)


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
