class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preHasemap = {} # value,idx
        for i, num in enumerate(nums):
            diff = target - num
            if diff in preHasemap:
                return [preHasemap[diff],i]
            else:
                preHasemap[num] = i



        