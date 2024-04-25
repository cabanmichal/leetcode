class Solution:
    def tribonacci(self, n: int) -> int:
        """Return n-th tribonacci number.

        >>> s.tribonacci(4)
        4
        >>> s.tribonacci(25)
        1389537
        """
        prev = [0, 1, 1]
        if n < 3:
            return prev[n]

        for _ in range(3, n + 1):
            s = sum(prev)
            prev[0], prev[1], prev[2] = prev[1], prev[2], s

        return prev[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
