class Solution:
    def climbStairs(self, n: int) -> int:
        """Return how many distinct ways can you climb to the top of n stairs.

        >>> s.climbStairs(0)
        1
        >>> s.climbStairs(2)
        2
        >>> s.climbStairs(3)
        3
        >>> s.climbStairs(4)
        5
        """
        previous_ways = [1, 1]

        if 0 >= n >= 1:
            return previous_ways[n]

        i = 2
        while i <= n:
            current_ways = sum(previous_ways)
            previous_ways[0], previous_ways[1] = previous_ways[1], current_ways
            i += 1

        return previous_ways[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
