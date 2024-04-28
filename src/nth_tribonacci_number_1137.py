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

        for i in range(3, n + 1):
            for j in [1, 2]:
                prev[i % 3] += prev[(i - j) % 3]

        return prev[n % 3]


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
