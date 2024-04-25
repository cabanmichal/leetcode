class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """Return distinct elements in nums1 and nums2.

        >>> s.findDifference([1, 2, 3], [2, 4, 6])
        [[1, 3], [4, 6]]
        >>> s.findDifference([1, 2, 3, 3], [1, 1, 2])
        [[3], []]
        """

        def distinct(nums1: list[int], nums2: list[int]) -> list[int]:
            i, end1 = 0, len(nums1)
            j, end2 = 0, len(nums2)
            d: list[int] = []

            while i < end1:
                while j < end2 and nums2[j] < nums1[i]:
                    j += 1
                if (j >= end2 or nums2[j] != nums1[i]) and (
                    d and d[-1] != nums1[i] or not d
                ):
                    d.append(nums1[i])

                i += 1

            return d

        s1 = sorted(nums1)
        s2 = sorted(nums2)

        return [distinct(s1, s2), distinct(s2, s1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
