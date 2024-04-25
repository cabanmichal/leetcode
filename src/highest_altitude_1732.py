class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """Return the highest altitude of a point.

        >>> s.largestAltitude([-5, 1, 5, 0, -7])
        1
        >>> s.largestAltitude([-4, -3, -2, -1, 4, 3, 2])
        0
        """
        max_so_far, current = 0, 0

        for g in gain:
            current += g
            if current > max_so_far:
                max_so_far = current

        return max_so_far


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
