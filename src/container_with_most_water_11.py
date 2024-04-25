class Solution:
    def maxArea(self, height: list[int]) -> int:
        """Return the maximum amount of water a container can store.

        >>> s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        >>> s.maxArea([1, 1])
        1
        >>> s.maxArea([1, 2, 4, 3])
        4
        >>> s.maxArea([1, 3, 2, 5, 25, 24, 5])
        24
        >>> s.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        25
        >>> s.maxArea([9, 6, 14, 11, 2, 2, 4, 9, 3, 8])
        72
        """

        def area(i: int, j: int) -> int:
            return (j - i) * min(height[i], height[j])

        i, j = 0, len(height) - 1
        max_so_far = 0

        while i < j:
            max_so_far = max(max_so_far, area(i, j))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_so_far


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
