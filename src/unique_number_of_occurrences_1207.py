from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """Verify if the number of occurrences of each value is unique.

        >>> s.uniqueOccurrences([1, 2, 2, 1, 1, 3])
        True
        >>> s.uniqueOccurrences([1, 2])
        False
        >>> s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
        True
        """
        counts = list(Counter(arr).values())

        return len(counts) == len(set(counts))


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
