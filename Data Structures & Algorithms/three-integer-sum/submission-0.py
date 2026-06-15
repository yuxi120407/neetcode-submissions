class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        print(sorted_nums)
        for i, n in enumerate(sorted_nums):
            if i>0 and n==sorted_nums[i-1]:
                continue
            print(n)
            l = i+1
            r = len(sorted_nums)-1
            while l<r:
                threesum = n + sorted_nums[l] + sorted_nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([n,sorted_nums[l],sorted_nums[r]])
                    l+=1
                    r-=1
                    while sorted_nums[l]==sorted_nums[l-1] and l<r:
                        l+=1
        return res



        