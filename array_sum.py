Method 1:
# Python 3 code to find sum of elements in given array 
def _sum(arr,n): 
      
    # return sum using sum  
    # inbuilt sum() function 
    return(sum(arr)) 
  
# driver function 
arr=[] 
# input values to list 
arr = [12, 3, 4, 15] 
  
# calculating length of array 
n = len(arr) 
  
ans = _sum(arr,n) 
  
# display sum 
print ('Sum of the array is ', ans) 
----------------------------------------
Method 2:
# Python 3 code to find sum of elements in given array driver function 
arr = [] 
  
# input values to list 
arr = [12, 3, 4, 15] 
  
# sum() is an inbuilt function in python that adds all the elements in list,set and tuples and returns the value  
ans = sum(arr) 
  
# display sum 
print ('Sum of the array is ',ans)

OUTPUT: Sum of the array is  34
