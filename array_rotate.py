METHOD-1(Using temp array)

Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]

------------------------------------------

METHOD-2 (Rotate one by one)

leftRotate(arr[], d, n)
start
  For i = 0 to i < d
    Left rotate all elements of arr[] by one
end

----------------------------------------

#Function to left rotate arr[] of size n by d*/ 
def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  
#Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i+1] 
    arr[n-1] = temp 
          
  
# utility function to print an array */ 
def printArray(arr,size): 
    for i in range(size): 
        print ("%d"% arr[i],end=" ") 
  
   
# Driver program to test above functions */ 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 

OUTPUT: 3 4 5 6 7 1 2

-----------------------------------------

METHOD 3 (A Juggling Algorithm)

#Function to left rotate arr[] of size n by d 
def leftRotate(arr, d, n): 
    for i in range(gcd(d,n)): 
          
        # move i-th values of blocks  
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 
  
#UTILITY FUNCTIONS 
#function to print an array  
def printArray(arr, size): 
    for i in range(size): 
        print ("%d" % arr[i], end=" ") 
   
#Function to get gcd of a and b 
def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a%b) 
   
# Driver program to test above functions  
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 