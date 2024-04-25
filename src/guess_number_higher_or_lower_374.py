class Solution:
    def __init__(self) -> None:
        self.n = 1

    def guess(self, g: int) -> int:
        """Asses the guess.
        >>> s.n = 10
        >>> s.guess(5)
        1
        >>> s.guess(12)
        -1
        >>> s.guess(10)
        0
        """
        if g < self.n:
            return 1
        if g > self.n:
            return -1
        return 0

    def guessNumber(self, n: int) -> int:
        """Guess the number between 1 and n.
        >>> s.n = 6
        >>> s.guessNumber(10)
        6
        >>> s.n = 1
        >>> s.guessNumber(1)
        1
        >>> s.n = 1
        >>> s.guessNumber(2)
        1
        """
        left, right = 1, n

        while g := (left + right) // 2:
            a = self.guess(g)

            if a == -1:
                right = g - 1
            elif a == 1:
                left = g + 1
            else:
                break

        return g


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
