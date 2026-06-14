class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_element = 1
        postfix_element = 1
        prefix = []
        postfix = []
        new_arr = []
        for i in range(len(nums)):
            prefix_element*=nums[i]
            print(prefix_element)
            prefix.append(prefix_element)


        for j in range(len(nums)-1,-1,-1):
            postfix_element*=nums[j]
            print(postfix_element)
            postfix.append(postfix_element)
        
        postfix = postfix[::-1]
        print(postfix)
        print(prefix)
        
        for k in range(len(nums)):
            if k==0:
                item_new = 1*postfix[k+1]
            elif k==len(nums)-1:
                item_new = prefix[k-1]*1
            else:
                item_new = prefix[k-1]*postfix[k+1]
            new_arr.append(item_new)
        return new_arr
            



        