class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """Return the minimum cost to reach the top of the floor.

        >>> s.minCostClimbingStairs([10, 15, 20])
        15
        >>> s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        6
        """
        previous_costs = [0, 0]
        start = len(cost) - 1
        i = start

        while i >= 0:
            current_cost = cost[i]
            if i < start - 1:
                current_cost += min(*previous_costs)
            previous_costs[0], previous_costs[1] = current_cost, previous_costs[0]
            i -= 1

        return min(*previous_costs)


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"s": Solution()})
