class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """Return kids with the greatest number of candies.

        >>> s.kidsWithCandies([2, 3, 5, 1, 3], 3)
        [True, True, True, False, True]
        >>> s.kidsWithCandies([4, 2, 1, 1, 2], 1)
        [True, False, False, False, False]
        >>> s.kidsWithCandies([12, 1, 12], 10)
        [True, False, True]
        """
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
