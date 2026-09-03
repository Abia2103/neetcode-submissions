class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = dict()
        for i in range(0,len(nums)):
            if (nums[i] in hash):
                return True
            else:
                hash.update({
                    nums[i]:i
                })
        return False