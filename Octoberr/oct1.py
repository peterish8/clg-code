def maxSubArray(nums):   
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):   
        num = nums[i]              
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
a = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
print(maxSubArray(a))
