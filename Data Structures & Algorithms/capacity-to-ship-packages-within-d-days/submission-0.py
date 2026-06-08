class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left<right:
            mid = (left+right)//2

            days_needed = 1
            current_weights = 0

            for weight in weights:
                if current_weights + weight > mid:
                    days_needed+=1
                    current_weights = 0

                current_weights += weight

            if days_needed <= days:
                right = mid
            else:
                left = mid + 1

        return left                
        