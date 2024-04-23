class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Verify that s is a subsequence of t.

        >>> s.isSubsequence("ace", "abcde")
        True
        >>> s.isSubsequence("aec", "abcde")
        False
        >>> s.isSubsequence("abc", "ahbgdc")
        True
        >>> s.isSubsequence("axc", "ahbgdc")
        False
        >>> s.isSubsequence("aaaaaa", "bbaaaa")
        False
        """
        i, end = 0, len(t)
        for c in s:
            while i < end:
                # character found in t, let's try to find the next one
                if t[i] == c:
                    i += 1
                    break
                i += 1
            else:  # character not found in t
                return False

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
