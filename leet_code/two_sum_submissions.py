def twoSum_brute_force(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        
        return None

#optimized solution
def twoSum(self, nums:list, target: int) -> list:
        helper_dict ={}
        
        if len(nums) == 2 and nums[0] == nums[1]:
            return [0,1]
        else:
            for i,elem in enumerate(nums):
                helper_dict[elem] = i
                
            for i,elem in enumerate(nums):
                reminder = target - elem
                if reminder in helper_dict and helper_dict[reminder] != i:
            
                    return [helper_dict[reminder],i]

                helper_dict[elem] = i

            return [-1,-1]