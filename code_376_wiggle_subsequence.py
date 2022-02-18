class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        positive = [1] * n
        negative = [1] * n
        for i in range(1, n):
            current_diff = nums[i] - nums[i-1]
            if current_diff > 0:
                positive[i] = negative[i-1] +1
                negative[i] = negative[i-1]
            elif current_diff < 0:
                positive[i] = positive[i-1]
                negative[i] = positive[i-1] + 1
            else:
                positive[i] = positive[i-1]
                negative[i] = negative[i-1]
        return max(positive[n-1], negative[n-1])