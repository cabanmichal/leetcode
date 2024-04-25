class RecentCounter:

    def __init__(self):
        self.requests = []
        self.i = 0

    def ping(self, t: int) -> int:
        """Add a request and return number of requests within last 3000 ms.

        >>> c.ping(1)
        1
        >>> c.ping(100)
        2
        >>> c.ping(3001)
        3
        >>> c.ping(3002)
        3
        """
        self.requests.append(t)

        i = self.i
        while i < len(self.requests) and t - 3000 > self.requests[i]:
            i += 1
        self.i = i

        return len(self.requests) - i


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"c": RecentCounter()})
