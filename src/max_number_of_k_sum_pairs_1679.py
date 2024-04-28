class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """Return the maximum number of operations you can perform on the array.

        In one operation, you can pick two numbers from the array whose sum equals k
        and remove them from the array.

        >>> s.maxOperations([1, 2, 3, 4], 5)
        2
        >>> s.maxOperations([3, 1, 3, 4, 3], 6)
        1
        """
        nums_sorted = sorted(nums)
        count = 0
        i, j = 0, len(nums) - 1

        while i < j:
            s = nums_sorted[i] + nums_sorted[j]

            if s < k:
                i += 1
            elif s > k:
                j -= 1
            else:
                i += 1
                j -= 1
                count += 1

        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
