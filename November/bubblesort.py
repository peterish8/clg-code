def swap(arr1,i,j):
    temp = arr1[i]
    arr1[i] = arr1[j]
    arr1[j] = temp


def sortbubble(arr1):
    len1 = len(arr1)
    for i in range(len1):
        for j in range(1,len1-i):
            if arr1[j-1] > arr1[j]:
                swap(arr1,j-1,j)
    return arr1
arr1 = [3,9,7,1,6,0,6,3]
print(sortbubble(arr1))