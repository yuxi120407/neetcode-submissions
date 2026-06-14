class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums = sorted(set(nums))
            i = 0
            best = 0
            while i<=len(nums):
                j = i
                while j<(len(nums)-1):
                    if nums[j]+1==nums[j+1]:
                        j+=1
                    else:
                        break

                best = max(j+1-i, best)
                i = j +1
        else:
            return 0
            

        return best
 
        