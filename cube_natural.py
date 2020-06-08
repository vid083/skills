# Simple Python program to find sum of series with cubes of first n natural numbers 
  
# Returns the sum of series  
def sumOfSeries(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i 
          
    return sum
  
   
# Driver Function 
n = 5
print(sumOfSeries(n)) 

--------------------------------------
# Returns the sum of series
def sumOfSeries(n): 
    x = (n * (n + 1)  / 2) 
    return (int)(x * x) 
--------------------------------------

# Returns the sum of series  
def sumOfSeries(n): 
    x = 0
    if n % 2 == 0 :  
        x = (n/2) * (n+1) 
    else: 
        x = ((n + 1) / 2) * n 
          
    return (int)(x * x) 

    OUTPUT:  225
