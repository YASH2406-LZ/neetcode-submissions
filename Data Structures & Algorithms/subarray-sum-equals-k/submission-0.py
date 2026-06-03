class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = 0
        prefix = {0:1}
        count = 0 

        for n in nums:
            cursum += n

            if cursum - k in prefix:
                count += prefix[cursum - k]

            prefix[cursum] = prefix.get(cursum,0) + 1

        return count    
        
        

        