Python Program to check if given array is Monotonic

Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return “True” if the given array A is monotonic else return “False” (without quotes).

Examples:
Input : 6 5 4 4
Output : true

Input : 5 15 20 10
Output : false

# Python3 program to find sum in Nth group 
  
# Check if given array is Monotonic 
def isMonotonic(A): 
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
  
# Driver program 
A = [6, 5, 4, 4] 
  
# Print required result 
print(isMonotonic(A)) 

Output : true
