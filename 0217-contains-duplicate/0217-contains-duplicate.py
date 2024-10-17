class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()     # O(Nlog(N))

        for i in range(len(nums) - 1):    # O(N)
            if nums[i] == nums[i + 1]:
                return True
        return False
    