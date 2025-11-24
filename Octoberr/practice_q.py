# u have a numebr lets say 24, in a pre defined array if factors of
# its not there raise exception no factors, if there and if its 
# is not prime then raise exception factors is not prime , 
# if after all these things if left thene print (use functions ) 
# and call the function that manner


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def get_user_array():
    array = []
    user_input = input("Enter numbers separated by space: ")
    numbers = user_input.split()
    
    for num in numbers:
        try:
            value = int(num)
            array.append(value)
        except:
            print("non integer input")
            break
    
    return array

def check_number(number, array):
    factors = get_factors(number)
    
    found = []
    for f in factors:
        if f in array:
            found.append(f)
    
    if len(found) == 0:
        print("no factors")
    
    for f in found:
        if is_prime(f) == False:
            print("factors is not prime")
            break
    
    print("Valid factors:", found)

number = 24

try:
    array = get_user_array()
    check_number(number, array)
except Exception as e:
    print("Exception:", e)


    


    '''
    
    
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def get_user_array():
    array = []
    user_input = input("Enter numbers separated by space: ")
    numbers = user_input.split()
    
    for num in numbers:
        try:
            value = int(num)
            array.append(value)
        except:
            raise Exception("non integer input")
    
    return array

def check_number(number, array):
    factors = get_factors(number)
    
    found = []
    for f in factors:
        if f in array:
            found.append(f)
    
    if len(found) == 0:
        raise Exception("no factors")
    
    for f in found:
        if is_prime(f) == False:
            raise Exception("factors is not prime")
    
    print("Valid factors:", found)

number = 24

try:
    array = get_user_array()
    check_number(number, array)
except Exception as e:
    print("Exception:", e)


    '''