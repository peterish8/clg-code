#Exception for 0 and negative sum

numbers = [2, -3, 1]  
print("Numbers in list:", numbers)
print("All possible subarrays and their sums:")
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        subarray = numbers[i:j+1]     
        sub_sum = sum(subarray)       
        print("Subarray:", subarray, "=> Sum:", sub_sum)
        try:
            if sub_sum == 0:
                print("The sum of this subarray is ZERO!")
        except:
            print("Something went wrong while checking for ZERO sum!")
        try:
            if sub_sum < 0:
                print("The sum of this subarray is NEGATIVE!")
        except:
            print("Something went wrong while checking for NEGATIVE sum!")
