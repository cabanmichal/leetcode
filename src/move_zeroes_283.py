class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """Move all 0's to the end of the list while maintaining the relative
        order of other elements.

        >>> a = [0, 1, 0, 3, 12]
        >>> s.moveZeroes(a)
        >>> a
        [1, 3, 12, 0, 0]
        >>> a = [0]
        >>> s.moveZeroes(a)
        >>> a
        [0]
        >>> a = [1, 0, 1]
        >>> s.moveZeroes(a)
        >>> a
        [1, 1, 0]
        """
        i, j, index_max = 0, 0, len(nums)
        while i < index_max:
            # find non-zero
            while i < index_max and nums[i] == 0:
                i += 1

            # find zero for swap
            while j < i and nums[j] != 0:
                j += 1

            if i < index_max and j < i:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

            i += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
