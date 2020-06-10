# Python3 program to swap first and last element of a list 
Examples:
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
----------------------------------------
Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.

# Swap function 
def swapList(newList): 
    size = len(newList) 
      
    # Swapping  
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp 
      
    return newList 
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
  
print(swapList(newList)) 
-------------------------------------
Approach #2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].

# Swap function 
def swapList(newList): 
      
    newList[0], newList[-1] = newList[-1], newList[0] 
  
    return newList 
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
print(swapList(newList))
----------------------------------------
Approach #3: Swap the first and last element is using tuple variable. Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with first and last element in that list. Now, the First and last values in that list are swapped.

# Swap function 
def swapList(list): 
      
    # Storing the first and last element  
    # as a pair in a tuple variable get 
    get = list[-1], list[0] 
      
    # unpacking those elements 
    list[0], list[-1] = get 
      
    return list
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
print(swapList(newList)) 

OUTPUT: [24, 35, 9, 56, 12]
----------------------------------------
Approach #4: Using * operand.

# Python3 program to illustrate  
# the usage of * operarnd 
list = [1, 2, 3, 4] 
  
a, *b, c = list
  
print(a) 
print(b) 
print(c)

OUTPUT:
1
[2, 3]
4
-----------------------------------------
Approach #5: Swap the first and last elements is to use inbuilt function list.pop(). 

# Swap function 
def swapList(list): 
      
    first = list.pop(0)    
    last = list.pop(-1) 
      
    list.insert(0, last)   
    list.append(first)    
      
    return list
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
  
print(swapList(newList)) 

OUTPUT: 

