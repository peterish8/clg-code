'''
def runningSum(nums):
    ans = [0] * len(nums)
    ans[0] = nums[0]             
    for i in range(1, len(nums)):
        ans[i] = ans[i-1] + nums[i]  
    return ans

print(runningSum([1, 2, 3, 4]))  
'''

d1 = {}
l1 = [5,4,5,3,3,5,4,4,7,7]
for i in l1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)


