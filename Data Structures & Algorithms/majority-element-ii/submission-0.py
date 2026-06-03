class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        result = []
        threshold = len(nums) // 3

    # Step 1: Count frequency of every element
        for num in nums:
            count[num] = count.get(num, 0) + 1

    # Step 2: Check if frequency > n/3
        for num, freq in count.items():
            if freq > threshold:
                result.append(num)

        return result


    
        