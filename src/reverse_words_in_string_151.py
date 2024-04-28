class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse the order of the words in s.
        >>> s.reverseWords("the sky is blue")
        'blue is sky the'
        >>> s.reverseWords("  hello world  ")
        'world hello'
        >>> s.reverseWords("a good   example")
        'example good a'
        """

        return " ".join(reversed(s.split()))


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
