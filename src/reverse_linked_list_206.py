from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(numbers: list[int]) -> Optional["ListNode"]:
        if not numbers:
            return None

        nodes = [ListNode(n) for n in numbers]

        i = 0
        while i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
            i += 1

        return nodes[0]

    @staticmethod
    def to_list(head: Optional["ListNode"]) -> list[int]:
        """Convert ListNode to List of integers.

        >>> ListNode.to_list(ListNode.from_list([1, 2, 3]))
        [1, 2, 3]
        >>> ListNode.to_list(ListNode.from_list([]))
        []
        """
        numbers = []

        current = head
        while current is not None:
            numbers.append(current.val)
            current = current.next

        return numbers


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """Reverse the singly linked list.
        >>> head = ListNode.from_list([1, 2, 3, 4, 5])
        ...
        >>> ListNode.to_list(s.reverseList(head))
        [5, 4, 3, 2, 1]
        >>> head = ListNode.from_list([1, 2])
        ...
        >>> ListNode.to_list(s.reverseList(head))
        [2, 1]
        >>> head = ListNode.from_list([])
        ...
        >>> ListNode.to_list(s.reverseList(head))
        []
        """
        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
