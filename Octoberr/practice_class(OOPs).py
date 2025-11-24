# u have a numebr lets say 24, in a pre defined array if factors of
# its not there raise exception no factors, if there and if its 
# is not prime then raise exception factors is not prime , 
# if after all these things if left thene print (use functions ) 
# and call the function that manner
'''
def factor(num,n):
    if n%num == 0:
        return True 
    return False

def primeNumber(num,n):
    if n<=1:
        return False
    for i in range(2,num**0.5+1):
        if n%i == 0:
            return False
    return True

def printexception():
    n = int(input("Enter a number"))
    try:
        arr = list(map(int,input().split()))
        try:
            for i in arr:
                if factor(i,n):
                    if primeNumber(i):
                        print("Valid factor:",i)
        except:
            raise Exception("Factor is not prime")
    except:
        raise Exception("No factors found")
    
            

'''
