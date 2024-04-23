class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """Verify that n flowers can be planted in the flowerbed.

        >>> s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
        True
        >>> s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
        False
        >>> s.canPlaceFlowers([0], 1)
        True
        """
        # flowerbed = flowerbed.copy()
        can_plant = 0
        width = 3
        start = 0
        end = len(flowerbed) - width

        if len(flowerbed) < width:
            if 1 not in flowerbed:
                can_plant = 1
        else:
            for i in range(start, end + 1):
                if i == start and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    can_plant += 1

                if i == end and flowerbed[i + 1] == 0 and flowerbed[i + 2] == 0:
                    flowerbed[i + 2] = 1
                    can_plant += 1

                if (
                    flowerbed[i] == 0
                    and flowerbed[i + 1] == 0
                    and flowerbed[i + 2] == 0
                ):
                    flowerbed[i + 1] = 1
                    can_plant += 1

        return can_plant >= n


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
