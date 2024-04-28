class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Return the max number of vowels in any substring of s with length k.
        >>> s.maxVowels("emkzcblopdxxtbxnxkevjqumgtivb", 5)
        2
        >>> s.maxVowels("pdzndkhhoujpqyex", 5)
        2
        >>> s.maxVowels("weallloveyou", 7)
        4
        >>> s.maxVowels("abciiidef", 3)
        3
        >>> s.maxVowels("aeiou", 2)
        2
        >>> s.maxVowels("leetcode", 3)
        2
        """
        vowels = set("aeiou")

        max_count, count = 0, 0
        i, j, end = 0, 0, len(s)

        while i < end:
            while j < end and j < i + k:
                if s[j] in vowels:
                    count += 1
                j += 1

            max_count = max(max_count, count)
            if max_count == k:
                break

            if s[i] in vowels:
                count -= 1

            i += 1

        return max_count


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
