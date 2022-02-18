class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return 0
        dp = [1] * n
        dp[1] = 2 if nums[0] != nums[1] else 1


        #note - add in the possibility of skipping some values
        p0=0
        for i in range(2, n):
            p0=i-2
            current_diff = nums[i] - nums[i-1]
            previous_diff = nums[i-1] - nums[i-2]
            is_wiggling = (current_diff < 0 and previous_diff > 0) or (current_diff > 0 and previous_diff < 0)
            max_wiggle = dp[i-1] if is_wiggling else 0
            
            while p0>=1:
                current_diff = nums[i] - nums[p0]
                previous_diff = nums[p0] - nums[p0-1]
                is_wiggling = (current_diff < 0 and previous_diff > 0) or (current_diff > 0 and previous_diff < 0)
                if is_wiggling:
                    max_wiggle = max(max_wiggle, dp[p0])
                p0 -= 1
            
            if max_wiggle > 0:
                dp[i] = max_wiggle + 1

        return max(dp)