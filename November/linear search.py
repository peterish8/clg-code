# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:  
#             return i          
#     return -1  
# numbers = [4, 10, 2, 15, 8, 20]
# item = 15
# result = linear_search(numbers, item)
# print(result)







# def prime(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def secprime(arr):
#     c = 0
#     for i in range(len(arr)):
#         if prime(arr[i]):
#             c += 1
#             if c == 2:
#                 return i
#     return -1
# arr = [4,6,7,8,10,3,12,54,1]
# print(secprime(arr))





# def binarysearch(arr):
#     l,r = 0,len(arr)-1
#     while l<=r:
#         m = (l+r)//2
#         if arr[m] == target:
#             return m
#         elif arr[m] < target :
#             l = m+1
#         else:
#             r = m-1
#     return -1
# arr = [2,5,9,11,16,21,24]
# target = 16
# print(binarysearch(arr))








def searchbinary(arr,t):
  left,right = 0,len(arr)-1
  while left <=right:
    mid = (left+right)//2
    if arr[mid] == t:
      return mid
    elif arr[mid] < t:
      left = mid +1
    elif arr[mid] > t:
      right = mid-1
  return -1
arr = [2,5,9,11,16,21,27]
target = 16
print(searchbinary(arr,target))
