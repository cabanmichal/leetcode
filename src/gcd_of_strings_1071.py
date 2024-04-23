class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Return greatest common divisor of two strings.

        >>> s.gcdOfStrings("ABCABC", "ABC")
        'ABC'
        >>> s.gcdOfStrings("ABABAB", "ABAB")
        'AB'
        >>> s.gcdOfStrings("LEET", "CODE")
        ''
        >>> s.gcdOfStrings("TEXXTEXXTEXX", "TEXXTEXX")
        'TEXX'
        """
        shorter, longer = str1, str2
        if len(shorter) > len(longer):
            shorter, longer = longer, shorter

        while True:
            reminders = [s for s in longer.split(shorter) if s]

            if not reminders:
                return shorter

            if reminders[0] == longer:
                return ""

            shorter, longer = reminders[0], shorter


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
