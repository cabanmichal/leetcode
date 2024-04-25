class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """Calculate pivot index of the nums list.

        >>> s.pivotIndex([1, 7, 3, 6, 5, 6])
        3
        >>> s.pivotIndex([1, 2, 3])
        -1
        >>> s.pivotIndex([2, 1, -1])
        0
        """
        left, right = 0, sum(nums)

        for i, n in enumerate(nums):
            right -= n
            if i > 0:
                left += nums[i - 1]
            if left == right:
                return i

        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
