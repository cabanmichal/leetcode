class Solution:
    def reverseVowels(self, s: str) -> str:
        """Reverse vowels in a string.

        >>> s.reverseVowels("hello")
        'holle'
        >>> s.reverseVowels("leetcode")
        'leotcede'
        """
        chars = list(s)
        vowels = set("aeiou")
        i, j = 0, len(chars) - 1

        while i < j:
            while i < j and chars[i].lower() not in vowels:
                i += 1

            while j > i and chars[j].lower() not in vowels:
                j -= 1

            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

        return "".join(chars)


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
