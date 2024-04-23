class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Merge the strings by adding letters in alternating order.

        >>> s.mergeAlternately("abc", "pqr")
        'apbqcr'
        >>> s.mergeAlternately("ab", "pqrs")
        'apbqrs'
        >>> s.mergeAlternately("abcd", "pq")
        'apbqcd'
        """

        def gen():
            words = [word1, word2]
            i = 0
            should_continue = True

            while should_continue:
                should_continue = False
                for word in words:
                    if i < len(word):
                        yield word[i]
                        should_continue = True
                i += 1

        return "".join(gen())


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
