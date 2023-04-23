class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        k = len(nums) - k
        return nums[k]
        