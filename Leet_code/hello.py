nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray( nums) -> int:
        sum = -999999
        total = 0
        for i in range(len(nums)):
            total = total + nums[i]
           # if total < 0:
            #    total = 0
            if total > sum:
                sum = total
        return sum            
        
print(maxSubArray(nums))        