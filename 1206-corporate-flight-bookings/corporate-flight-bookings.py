class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        ans = [0] * n

        for st, end, seats in bookings:
            ans[st - 1] += seats
            if end < n:
                ans[end] -= seats

        for i in range(1, n):
            ans[i] += ans[i - 1]

        return ans