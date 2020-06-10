Input: arr[] = {5, -1, -1, 1, 2, 3}, M = 7
Output: 5 6 0 1 2 3
M = 7, so value at index 2 should be (5+1) % 7 = 6
value at index 3 should be (6+1) % 7 = 0

Input: arr[] = {5, -1, 7, -1, 9, 0}, M = 10
Output: 5 6 7 8 9 0

# Python implementation of the above approach 
def construct(n, m, a): 
    ind = 0
  
    # Finding the index which is not -1 
    for i in range(n): 
        if (a[i]!=-1): 
            ind = i 
            break
  
    # Calculating the values of the indexes ind-1 to 0 
    for i in range(ind-1, -1, -1): 
        if (a[i]==-1): 
            a[i]=(a[i + 1]-1 + m)% m 
  
    # Calculating the values of the indexes ind + 1 to n 
    for i in range(ind + 1, n): 
        if(a[i]==-1): 
            a[i]=(a[i-1]+1)% m 
    print(*a) 
  
# Driver code 
n, m = 6, 7
a =[5, -1, -1, 1, 2, 3] 
construct(n, m, a) 