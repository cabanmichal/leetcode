from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Search for value in the tree.
        >>> t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        ...
        >>> s.searchBST(t, 2) == t.left
        True
        >>> s.searchBST(t, 5) is None
        True
        """
        if root is None:
            return None

        if val > root.val:
            return self.searchBST(root.right, val)

        if val < root.val:
            return self.searchBST(root.left, val)

        return root


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
