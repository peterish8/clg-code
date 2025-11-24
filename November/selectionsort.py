def find_min_index(arr, start):
    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

def swap(arr, i, min_index):
    arr[i], arr[min_index] = arr[min_index], arr[i]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = find_min_index(arr, i)
        swap(arr, i, min_index)

arr = [29, 10, 14, 37, 13]
selection_sort(arr)
print("Sorted array:", arr)










