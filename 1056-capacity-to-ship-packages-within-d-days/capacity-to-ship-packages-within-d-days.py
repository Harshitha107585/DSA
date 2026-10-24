class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left+right)//2

            day = 1
            total = 0

            for weight in weights:
                if total + weight > mid:
                    total = 0
                    day+=1
                total+=weight
            if day <= days:
                right = mid
            else:
                left = mid+1 
        return right                          