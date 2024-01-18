import collections

class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        prefix_sum_count = collections.defaultdict(int)
        prefix_sum_count[0] = 1
        ans = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum = curr_sum - k
            ans += prefix_sum_count[prefix_sum]
            prefix_sum_count[curr_sum] += 1

        return ans
