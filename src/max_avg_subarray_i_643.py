class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """Return maximum average value of subarray with k elements.

        >>> v = s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
        >>> print(f"{v:.2f}")
        12.75
        >>> v = s.findMaxAverage([5], 1)
        >>> print(f"{v:.2f}")
        5.00
        """
        i, end = 0, len(nums) - k + 1
        max_so_far, current = float("-inf"), 0

        while i < end:
            if i == 0:
                current = sum(nums[:k])
            else:
                current = current - nums[i - 1] + nums[i + k - 1]
            if max_so_far < current:
                max_so_far = current

            i += 1

        return max_so_far / k


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
